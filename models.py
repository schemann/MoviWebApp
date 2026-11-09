"""Database models: users and their favorite movies."""
from typing import List, Optional

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):  # pylint: disable=too-few-public-methods
    """A user of the website with a list of favorite movies."""

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    # Deleting a user deletes their movies too.
    movies: Mapped[List["Movie"]] = relationship(back_populates="user",
                                                 cascade="all, delete-orphan")

    def __repr__(self):
        """Return a debugging representation."""
        return f"<User id={self.id} name={self.name!r}>"

    def __str__(self):
        """Return the user's name."""
        return self.name


class Movie(db.Model):  # pylint: disable=too-few-public-methods
    """A favorite movie of one user, with details fetched from OMDb."""

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    director: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    year: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    poster_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    # Link Movie to User
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id", ondelete="CASCADE"),
                                         nullable=False)
    user: Mapped["User"] = relationship(back_populates="movies")

    def __repr__(self):
        """Return a debugging representation."""
        return f"<Movie id={self.id} name={self.name!r} user_id={self.user_id}>"

    def __str__(self):
        """Return the movie name with its year."""
        return f"{self.name} ({self.year})" if self.year else self.name
