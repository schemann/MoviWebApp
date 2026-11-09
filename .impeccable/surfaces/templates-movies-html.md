---
version: 1
slug: "templates-movies-html"
primary_target: "templates/movies.html"
related_targets: ["templates/index.html","templates/base.html","static/style.css"]
---

Scope: whole app shell (users page, a user's movie list, error pages). Visitor mode: Operate.
Audience: course graders and portfolio reviewers; job: pick/create a profile, add movies by title, rename, delete.
Constraints: routes, form fields and behaviour unchanged; plain Jinja + one CSS file; no Netflix look.

## Direction contract

THESIS: a favourites list is a collector's shelf of numbered editions, not a streaming catalogue; refuses the dark poster-grid default.
OWN-WORLD: cool grey shelf wall, white surfaces, near-black ink; every user owns one saturated edition colour (teal, cobalt, mustard, plum, moss, emerald, coral, slate) that paints their header and spines; condensed uppercase spine lettering (Big Shoulders Display) over a workhorse grotesk (Schibsted Grotesk) with tabular numerals; dark shelf plank lines.
STORY: the visitor sees people as spines on a shelf, opens one, and reads that person's numbered edition of films; adding prints a new edition number.
FIRST VIEWPORT: top bar with logo and Users link; on the list page a full-width band in the user's edition colour with "Movies for Deb" at display size and the edition count; add-movie form directly below; covers in a grid, each with its spine strip (vertical title, Nº 001) attached left.
FORM: collector's edition shelf, my rank 1 (pick card), seed d39f5497. Signature move: covers slide out from their spine on hover/focus.
FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
