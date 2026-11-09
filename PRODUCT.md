# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Primary audience: Masterschool graders and later portfolio reviewers (employers) who open the
GitHub project and run the app. They judge within minutes whether it reads as a deliberate
product. In-app users are people who share one installation ("Who is watching?" profiles), each
keeping their own list of favorite movies. Usage scene is not fixed: evening on a sofa or daytime
at a desk are both plausible.

## Product Purpose

MoviWeb lets a user pick or create a profile and keep a personal list of favorite movies. A movie
is added by title only; the app fetches year, director and poster from OMDb. Titles can be
corrected inline, movies removed. Success: the course bonus "visually appealing, cohesive UI" is
clearly met, and the app works flawlessly end to end.

## Positioning

A personal favorites shelf, not a streaming catalogue: every entry is something one person chose,
and each person's list is their own (renaming a movie affects only that list).

## Capabilities and Constraints

- Routes and behaviour are fixed by the course: `/` (users + add form), `POST /users`,
  `/users/<id>/movies` (GET list, POST add by title), `.../movies/<id>/update` (POST rename),
  `.../movies/<id>/delete` (POST), `/users/<id>` redirects to the list; 404/405/500 pages.
- Plain Flask + Jinja templates + one stylesheet in `static/`, no build step; runs in Codio
  (Python 3.11, port 5000). External CDNs are possible but not required.
- Data per movie: name, director, year, poster URL (OMDb, may be missing; series have no director).
- Flash messages report success and errors (OMDb not found/unreachable, empty input, DB failure).

## Brand Commitments

- Name in the UI: "MovieApp" (as in the course demo screenshot `downloads/moviweb-demo.png`).
- Must not read as a Netflix clone (no black-and-red streaming look-alike).

## Evidence on Hand

- Real OMDb posters for whatever users add; local sample data: user "Deb" with Titanic, Twister,
  Good Will Hunting, Breaking Bad.
- No testimonials, metrics or claims exist; none may be invented.

## Product Principles

1. The poster is the content: each movie is recognised by its artwork first.
2. Personal over catalogue: the UI speaks about one person's choices, not about "what's on".
3. Course behaviour is sacred: design never changes routes, fields or flows.
4. Works for a reviewer in two minutes: obvious first action, no dead ends, clear feedback.

## Accessibility & Inclusion

Keyboard operable, visible focus, labelled form fields, WCAG AA contrast, mobile width 390px.
