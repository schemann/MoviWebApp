"""Fetch movie details from the OMDb API (https://www.omdbapi.com)."""
import os
import re
from typing import Optional

import requests

OMDB_URL = "https://www.omdbapi.com/"
TIMEOUT_SECONDS = 10


class OmdbError(Exception):
    """Raised when OMDb gives no usable answer; the message is shown to the user."""


def _clean(value: Optional[str]) -> Optional[str]:
    """Return None for OMDb's 'N/A' placeholder and empty values."""
    if not value or value.strip() == "N/A":
        return None
    return value.strip()


def _parse_year(value: Optional[str]) -> Optional[int]:
    """Return the first four-digit year in OMDb's Year field ('1997', '2005-2010')."""
    match = re.search(r"\d{4}", value or "")
    return int(match.group()) if match else None


def fetch_movie(title: str) -> dict:
    """Look up a movie by title and return name, director, year and poster_url.

    The API key is read from the OMDB_API_KEY environment variable.
    Raises OmdbError if the key is missing, OMDb is unreachable or the movie is unknown.
    """
    api_key = os.environ.get("OMDB_API_KEY", "").strip()
    if not api_key:
        raise OmdbError("No OMDb API key configured. Set OMDB_API_KEY in the .env file.")
    try:
        response = requests.get(OMDB_URL, params={"apikey": api_key, "t": title},
                                timeout=TIMEOUT_SECONDS)
        data = response.json()
    except requests.RequestException as error:
        raise OmdbError("OMDb could not be reached. Please try again later.") from error
    except ValueError as error:
        raise OmdbError("OMDb sent an invalid answer. Please try again later.") from error

    if data.get("Response") != "True":
        message = data.get("Error", "Unknown error")
        if response.status_code == 401:
            raise OmdbError(f"OMDb rejected the API key: {message}")
        raise OmdbError(f"OMDb: {message} ({title})")
    return {
        "name": _clean(data.get("Title")) or title,
        "director": _clean(data.get("Director")),
        "year": _parse_year(data.get("Year")),
        "poster_url": _clean(data.get("Poster")),
    }
