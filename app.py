"""MoviWeb App: users keep a list of favorite movies, with details from OMDb."""
import os

from flask import Flask

from data_manager import DataManager
from models import db

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data', 'movies.db')}"

db.init_app(app)  # Link the database (db from models.py) to the app

data_manager = DataManager()  # Create an object of your DataManager class

# Create the tables on start-up, also under "flask run" (which skips __main__).
# create_all() only adds missing tables; existing data stays untouched.
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    """Temporary test route."""
    return "Welcome to MoviWeb App!"


@app.route('/users')
def list_users():
    """List all users (temporarily as plain text)."""
    users = data_manager.get_users()
    return str(users)  # Temporarily returning users as a string


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
