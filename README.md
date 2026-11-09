# MoviWeb App

A Flask web application where users register their name and keep a list of favorite
movies; movie details come from the OMDb API (Masterschool exercise).

## Run

```
pip install -r requirements.txt
cp .env.example .env   # then put your OMDb key into .env
python app.py          # or: flask run --host=0.0.0.0 --port=5000
```

Get a free OMDb key at https://www.omdbapi.com/apikey.aspx. The SQLite database is created
in `data/movies.db` on the first start.

## Routes

| Method | URL | Action |
|---|---|---|
| GET | `/` | list users, form to add a user |
| POST | `/users` | add a user |
| GET | `/users/<user_id>/movies` | a user's favorite movies |
| POST | `/users/<user_id>/movies` | add a movie by title (details from OMDb) |
| POST | `/users/<user_id>/movies/<movie_id>/update` | rename a movie |
| POST | `/users/<user_id>/movies/<movie_id>/delete` | remove a movie |
