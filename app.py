"""MoviWeb App: users keep a list of favorite movies, with details from OMDb."""
import os

from dotenv import load_dotenv
from flask import Flask, abort, flash, redirect, render_template, request, url_for

from data_manager import DatabaseError, DataManager
from models import db, Movie
from omdb import OmdbError, fetch_movie

load_dotenv()

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data', 'movies.db')}"
# Needed for flash messages; set SECRET_KEY in .env to keep sessions across restarts.
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY") or os.urandom(24)

db.init_app(app)  # Link the database (db from models.py) to the app

data_manager = DataManager()  # Create an object of your DataManager class

# Create the tables on start-up, also under "flask run" (which skips __main__).
# create_all() only adds missing tables; existing data stays untouched.
with app.app_context():
    db.create_all()


def get_user_or_404(user_id):
    """Return the user with this id or answer with 404."""
    user = data_manager.get_user(user_id)
    if user is None:
        abort(404)
    return user


def get_user_movie_or_404(user_id, movie_id):
    """Return the movie if it exists and belongs to this user, otherwise answer with 404."""
    movie = data_manager.get_movie(movie_id)
    if movie is None or movie.user_id != user_id:
        abort(404)
    return movie


@app.route('/')
def index():
    """Home page: all users and a form to add a new one."""
    users = data_manager.get_users()
    return render_template('index.html', users=users)


@app.route('/users', methods=['POST'])
def create_user():
    """Add a user from the form, then go back to the home page."""
    try:
        user = data_manager.create_user(request.form.get('name', ''))
    except ValueError as error:
        flash(str(error), 'error')
    except DatabaseError as error:
        app.logger.exception("Creating a user failed")
        flash(str(error), 'error')
    else:
        flash(f"Welcome, {user.name}!", 'success')
    return redirect(url_for('index'))


@app.route('/users/<int:user_id>')
def show_user(user_id):
    """Short URL for a user; leads to their movie list."""
    get_user_or_404(user_id)
    return redirect(url_for('list_movies', user_id=user_id))


@app.route('/users/<int:user_id>/movies', methods=['GET'])
def list_movies(user_id):
    """Show the favorite movies of one user."""
    user = get_user_or_404(user_id)
    movies = data_manager.get_movies(user_id)
    return render_template('movies.html', user=user, movies=movies)


@app.route('/users/<int:user_id>/movies', methods=['POST'])
def add_movie(user_id):
    """Look the title up on OMDb and add the movie to the user's favorites."""
    get_user_or_404(user_id)
    title = request.form.get('title', '').strip()
    if not title:
        flash("Please enter a movie title.", 'error')
        return redirect(url_for('list_movies', user_id=user_id))
    try:
        details = fetch_movie(title)
    except OmdbError as error:
        flash(str(error), 'error')
        return redirect(url_for('list_movies', user_id=user_id))
    try:
        movie = data_manager.add_movie(Movie(user_id=user_id, **details))
    except DatabaseError as error:
        app.logger.exception("Adding a movie failed")
        flash(str(error), 'error')
    else:
        flash(f"'{movie.name}' was added.", 'success')
    return redirect(url_for('list_movies', user_id=user_id))


@app.route('/users/<int:user_id>/movies/<int:movie_id>/update', methods=['POST'])
def update_movie(user_id, movie_id):
    """Rename a movie in the user's list (no OMDb lookup)."""
    get_user_movie_or_404(user_id, movie_id)
    try:
        movie = data_manager.update_movie(movie_id, request.form.get('title', ''))
    except ValueError as error:
        flash(str(error), 'error')
    except DatabaseError as error:
        app.logger.exception("Updating a movie failed")
        flash(str(error), 'error')
    else:
        flash(f"Title changed to '{movie.name}'.", 'success')
    return redirect(url_for('list_movies', user_id=user_id))


@app.route('/users/<int:user_id>/movies/<int:movie_id>/delete', methods=['POST'])
def delete_movie(user_id, movie_id):
    """Remove a movie from the user's favorites."""
    movie = get_user_movie_or_404(user_id, movie_id)
    name = movie.name
    try:
        data_manager.delete_movie(movie_id)
    except DatabaseError as error:
        app.logger.exception("Deleting a movie failed")
        flash(str(error), 'error')
    else:
        flash(f"'{name}' was removed.", 'success')
    return redirect(url_for('list_movies', user_id=user_id))


@app.errorhandler(404)
def page_not_found(_error):
    """Show a friendly page for unknown URLs, users and movies."""
    return render_template('404.html'), 404


@app.errorhandler(405)
def method_not_allowed(_error):
    """Show a friendly page when a form URL is opened directly in the browser."""
    return render_template('405.html'), 405


@app.errorhandler(500)
def internal_error(_error):
    """Roll back a failed transaction and show a friendly error page."""
    db.session.rollback()
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
