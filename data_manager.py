"""DataManager: all reads and writes of users and movies go through this class."""
from typing import List, Optional

from sqlalchemy.exc import SQLAlchemyError

from models import db, User, Movie


class DatabaseError(Exception):
    """Raised when a write to the database fails; the session has been rolled back."""


def _commit():
    """Commit the session; on failure roll back and raise DatabaseError."""
    try:
        db.session.commit()
    except SQLAlchemyError as error:
        db.session.rollback()
        raise DatabaseError("The database could not save the change.") from error


class DataManager:
    """CRUD operations for users and their favorite movies, using SQLAlchemy ORM."""

    def create_user(self, name: str) -> User:
        """Add a new user and return it; raises ValueError for an empty name."""
        name = (name or "").strip()
        if not name:
            raise ValueError("User name must not be empty.")
        user = User(name=name)
        db.session.add(user)
        _commit()
        return user

    def get_users(self) -> List[User]:
        """Return all users, sorted by name."""
        return db.session.execute(
            db.select(User).order_by(db.func.lower(User.name))
        ).scalars().all()

    def get_user(self, user_id: int) -> Optional[User]:
        """Return the user with this id, or None."""
        return db.session.get(User, user_id)

    def get_movies(self, user_id: int) -> List[Movie]:
        """Return all movies of one user, sorted by title."""
        return db.session.execute(
            db.select(Movie).where(Movie.user_id == user_id)
            .order_by(db.func.lower(Movie.name))
        ).scalars().all()

    def get_movie(self, movie_id: int) -> Optional[Movie]:
        """Return the movie with this id, or None."""
        return db.session.get(Movie, movie_id)

    def add_movie(self, movie: Movie) -> Movie:
        """Add a movie (already filled with its OMDb details and user_id) and return it."""
        if not movie.name or not movie.name.strip():
            raise ValueError("Movie title must not be empty.")
        if self.get_user(movie.user_id) is None:
            raise ValueError(f"There is no user with id {movie.user_id}.")
        db.session.add(movie)
        _commit()
        return movie

    def update_movie(self, movie_id: int, new_title: str) -> Optional[Movie]:
        """Rename a movie and return it, or None if it does not exist.

        Raises ValueError for an empty title.
        """
        new_title = (new_title or "").strip()
        if not new_title:
            raise ValueError("Movie title must not be empty.")
        movie = self.get_movie(movie_id)
        if movie is None:
            return None
        movie.name = new_title
        _commit()
        return movie

    def delete_movie(self, movie_id: int) -> bool:
        """Delete a movie from its user's favorites; return False if it did not exist."""
        movie = self.get_movie(movie_id)
        if movie is None:
            return False
        db.session.delete(movie)
        _commit()
        return True
