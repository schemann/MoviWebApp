---
name: MovieApp
description: A collector's shelf of numbered editions; every user owns one edition colour.
colors:
  wall: "#e9ecef"
  wall-deep: "#dde1e6"
  surface: "#ffffff"
  ink: "#16181d"
  ink-soft: "#4a515c"
  line: "#c9cfd6"
  plank: "#16181d"
  ok: "#0e6e4f"
  ok-bg: "#e2f2ea"
  err: "#a32637"
  err-bg: "#fbe6e9"
  edition-teal: "#0b6b6b"
  edition-teal-soft: "#d4ecec"
  edition-cobalt: "#2b45b0"
  edition-cobalt-soft: "#dbe1fa"
  edition-mustard: "#e0a526"
  edition-mustard-soft: "#3b2c06"
  edition-plum: "#6a2c6e"
  edition-plum-soft: "#ecd9ee"
  edition-moss: "#46601f"
  edition-moss-soft: "#e1ebcf"
  edition-coral: "#c2405a"
  edition-coral-soft: "#ffe3e8"
  edition-slate: "#3d4f66"
  edition-slate-soft: "#dce4ee"
  edition-emerald: "#0e6e4f"
  edition-emerald-soft: "#d3eee4"
typography:
  display:
    fontFamily: "Big Shoulders Display, Arial Narrow, sans-serif"
    fontSize: "clamp(2.6rem, 7vw, 5.2rem)"
    fontWeight: 800
    lineHeight: 0.92
    letterSpacing: "0.005em"
  brand:
    fontFamily: "Big Shoulders Display, Arial Narrow, sans-serif"
    fontSize: "1.9rem"
    fontWeight: 800
    lineHeight: 1
    letterSpacing: "0.01em"
  spine:
    fontFamily: "Big Shoulders Display, Arial Narrow, sans-serif"
    fontSize: "2rem"
    fontWeight: 800
    lineHeight: 1
    letterSpacing: "0.02em"
  numeral:
    fontFamily: "Big Shoulders Display, Arial Narrow, sans-serif"
    fontSize: "1.15rem"
    fontWeight: 700
    fontFeature: "tnum"
  title:
    fontFamily: "Schibsted Grotesk, system-ui, sans-serif"
    fontSize: "1.05rem"
    fontWeight: 700
    lineHeight: 1.5
  lede:
    fontFamily: "Schibsted Grotesk, system-ui, sans-serif"
    fontSize: "1.1rem"
    fontWeight: 400
    lineHeight: 1.5
  body:
    fontFamily: "Schibsted Grotesk, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.5
  caption:
    fontFamily: "Schibsted Grotesk, system-ui, sans-serif"
    fontSize: "0.78rem"
    fontWeight: 400
    lineHeight: 1.5
rounded:
  cover: "2px"
  spine: "3px"
  control: "4px"
spacing:
  xs: "8px"
  sm: "16px"
  md: "20px"
  lg: "28px"
  xl: "40px"
  2xl: "48px"
  3xl: "64px"
components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface}"
    typography: "{typography.body}"
    rounded: "{rounded.control}"
    padding: "10px 18px"
  button-primary-cobalt:
    backgroundColor: "{colors.edition-cobalt}"
    textColor: "{colors.surface}"
    rounded: "{rounded.control}"
    padding: "10px 18px"
  button-on-band:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.edition-cobalt}"
    rounded: "{rounded.control}"
    padding: "10px 18px"
  button-quiet:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "10px 18px"
  button-danger:
    textColor: "{colors.err}"
    padding: "10px 0"
  input-text:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.control}"
    padding: "10px 12px"
  notice-success:
    backgroundColor: "{colors.ok-bg}"
    textColor: "{colors.ok}"
    rounded: "{rounded.control}"
    padding: "10px 14px"
  notice-error:
    backgroundColor: "{colors.err-bg}"
    textColor: "{colors.err}"
    rounded: "{rounded.control}"
    padding: "10px 14px"
  panel:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.control}"
    padding: "{spacing.md}"
    width: "640px"
  user-spine:
    backgroundColor: "{colors.edition-cobalt}"
    textColor: "{colors.surface}"
    typography: "{typography.spine}"
    rounded: "{rounded.spine}"
    padding: "16px 8px 12px"
    width: "84px"
    height: "300px"
  edition-band:
    backgroundColor: "{colors.edition-cobalt}"
    textColor: "{colors.surface}"
    padding: "28px 16px 32px"
  cover-spine:
    backgroundColor: "{colors.edition-cobalt}"
    textColor: "{colors.surface}"
    rounded: "{rounded.cover}"
    width: "34px"
---

# Design System: MovieApp

## Overview

**Creative North Star: "The Collector's Edition Shelf"**

A favourites list is a shelf of numbered editions, not a streaming catalogue. The users page shows people as tall, flat, saturated book spines standing on a dark plank; opening one paints the page head in that person's edition colour and lays their films out as covers, each with a narrow spine strip attached at its left edge carrying the title in vertical capitals and an edition number. The rest of the world stays quiet: a cool grey wall, white working surfaces, near-black ink. Colour belongs to people, and posters supply everything else.

Density is calm and generous: one shelf row on the users page, a four-up cover grid on desktop and two-up on a 390px phone. Lettering carries the identity: a condensed uppercase display face for everything that reads as printed on a spine (headings, the wordmark, spine titles, edition numbers) over a sturdy grotesk for all working text. Motion is physical and small: spines lift off the shelf, covers slide out from their spine.

The world rejects the dark poster-grid default and the black-and-red streaming look (a binding brand commitment in PRODUCT.md). Near-black appears only as ink, the shelf plank and the default edition, never as a page ground.

**Key Characteristics:**
- Cool grey wall (`wall`) as the only page ground; white for working surfaces.
- One saturated edition colour per user, assigned by user id modulo 8, painting that user's spine, band, cover spines, primary buttons, focus ring and text selection.
- Condensed uppercase spine lettering (Big Shoulders Display) with tabular numerals; Schibsted Grotesk for everything operable.
- Edition numbers with a `Nº` prefix: two digits for users (`Nº 01`), three digits for films in id order (`Nº 001`).
- Dark plank lines under every shelf row: a 14px border under the users shelf, an 8px continuous plank under each cover row.
- Signature move: covers slide out from their spine on hover and focus.

**Open design opportunities (named by the finish review, not shipped).** These are ceiling items, not rules; nothing in the build evidences them yet:
- Criterion-style spine graphics (marks, rules or numbering systems printed on the spines beyond title and number).
- A new-edition slot at the end of the users shelf (an empty spine that invites adding a user, in place of the separate panel).
- World-bearing error and empty pages (404/405/500 and empty shelves currently use the plain page head and a plank line).
- Edition colour below the band on a user's page (today the colour stops at the band and the cover spines).

## Colors

A cool, nearly colourless room in which eight saturated edition inks do all the talking.

### Primary
The edition colours are the primary system: one per user, cycled by `user.id % 8` in this order: teal, cobalt, mustard, plum, moss, coral, slate, emerald. Each edition ships with a white text colour, except mustard, which takes `ink` text; each also has a paired soft ink (`*-soft`) for secondary text on the edition ground, chosen for at least 4.5:1.
- **Shelf Teal** (`edition-teal`), **Cobalt Edition** (`edition-cobalt`), **Mustard Cloth** (`edition-mustard`), **Plum Binding** (`edition-plum`), **Moss Board** (`edition-moss`), **Coral Jacket** (`edition-coral`), **Slate Linen** (`edition-slate`), **Emerald Edition** (`edition-emerald`): the spine on the users shelf, the full-bleed band on that user's page, every cover spine on that page, the primary button, the focus ring, the text caret and text selection.
- On the users page and the error pages, the edition defaults to `ink` with white text, so the primary button reads near-black there.

### Neutral
- **Cool Wall** (`wall`): the page ground everywhere, including the area behind the shelf.
- **Wall Shadow** (`wall-deep`): the placeholder ground of a cover that has no poster.
- **Paper White** (`surface`): panels, text inputs, the quiet button.
- **Shelf Ink** (`ink`): body text, headings, the active nav underline, the default edition.
- **Plank** (`plank`): shelf planks only; same value as ink, separate role.
- **Soft Ink** (`ink-soft`): ledes, fact values, empty-shelf copy, hovered input borders.
- **Hairline** (`line`): resting input border and quiet-button border.

### Status
- **Kept Green** (`ok` on `ok-bg`) and **Error Red** (`err` on `err-bg`): flash notices only; `err` also colours the Delete text button.

### Named Rules
**The Colour Belongs To People Rule.** Saturated colour appears only as a user's edition. Chrome, panels and page grounds stay neutral; a new surface earns colour only by belonging to someone.

**The One Edition Per Page Rule.** A user's page carries exactly one edition colour, set once on the page body; every edition-tinted element on that page inherits it.

## Typography

**Display Font:** Big Shoulders Display (with Arial Narrow, sans-serif), self-hosted variable woff2, OFL
**Body Font:** Schibsted Grotesk (with system-ui, sans-serif), self-hosted variable woff2, OFL

**Character:** Tall condensed capitals that look stamped on a book spine, set against a plain-spoken newsroom grotesk. The display face never sets a sentence; the grotesk never shouts.

### Hierarchy
- **Display** (800, fluid 2.6 to 5.2rem, line-height 0.92, uppercase, balanced wrap): the single page heading (`Users`, `Movies for Deb`, error titles).
- **Brand** (800, 1.9rem, uppercase): the MovieApp wordmark beside the logo.
- **Spine** (800, 2rem on desktop and 1.6rem on mobile, uppercase, vertical, bottom-to-top): user names on shelf spines; cover-spine titles use the same treatment at 1rem (0.8rem on mobile). Long names end in an ellipsis.
- **Numeral** (700, 1.15rem, tabular): edition numbers on spines; 1.3rem in the band, 0.85rem on cover spines.
- **Title** (700, 1.05rem): panel headings; editable film titles use 700 at 1.15rem.
- **Lede** (400, 1.1rem, `ink-soft`): the one sentence under a display heading.
- **Body** (400, 1rem, line-height 1.5): all working text, labels, buttons (700), nav (500). Fact values use tabular numerals.
- **Caption** (400, 0.78rem): the film count at the foot of a user spine.

### Named Rules
**The Spine Lettering Rule.** Big Shoulders Display is for things printed on a spine or a title page: page headings, the wordmark, spine titles and edition numbers. Forms, buttons, facts and messages are always Schibsted Grotesk.

**The Tabular Number Rule.** Every edition number, count and year is set with tabular numerals so stacked numbers align.

## Layout

One centred column, 1200px max, 16px side gutters; the top bar shares the same width. Page heads sit 28px below the bar with 32px under them.

- **Users shelf:** a single horizontal row of spines that scrolls sideways (snap to start) rather than wrapping, bottom-aligned on a 14px plank. Spines are 84 by 300px with a deliberate height rhythm (every third from the second is 330px, every fourth from the third is 280 by 96px) so the row reads as real books. 10px gaps, 28px headroom.
- **Edition band:** breaks out of the column to the full viewport width while its content stays aligned with the column.
- **Cover grid:** auto-fill columns of at least 230px, 40px row and 28px column gap; each cover is 2:3 with a 34px spine to its left. A plank under each cover extends 14px to both sides so planks join into one continuous line per row.
- **Add-user panel:** max 640px, 48px below the shelf.
- **Mobile (at or below 560px):** spines shrink to 64 by 230px (with the same rhythm at 250 and 215 by 72px), the shelf gets 24px headroom, the cover grid locks to two columns with 28px by 14px gaps, cover spines narrow to 24px and drop the `Nº` prefix, rename rows and fact rows stack.

### Named Rules
**The Shelf Row Rule.** Users stand in one row on one plank; the row scrolls, it never wraps into a grid.

## Elevation & Depth

Flat at rest; depth appears only when an object is picked up. Shadows are soft, ink-tinted (`rgba(22, 24, 29, …)`) and cast by the lifted object. Covers carry one faint resting shadow because they are physical prints.

### Shadow Vocabulary
- **Cover rest** (`0 2px 6px rgba(22, 24, 29, 0.18)`): every cover at rest.
- **Cover pulled** (`10px 12px 22px -8px rgba(22, 24, 29, 0.45)`): a cover sliding out of its spine.
- **Spine lifted** (`0 14px 20px -10px rgba(22, 24, 29, 0.55)`): a user spine raised off the shelf.
- **Button hover** (`0 4px 12px rgba(22, 24, 29, 0.18)`): filled buttons on hover; removed on press.

### Named Rules
**The Picked-Up Rule.** Spines, panels and buttons are flat at rest. Lift (translate plus shadow) is a response to hover or focus, never a resting state; covers keep only their faint print shadow.

## Shapes

Nearly square. Controls, notices and panels use a 4px radius; user spines round only their top corners (3px) and sit square on the plank; a cover spine and its cover share one 2px-rounded rectangle split down the seam. Spines are flat colour fields: no inset strips, bevels or gradients. Planks are hard-edged black bars. The only circle is the button loading spinner. Icons are authored inline SVG line drawings (1.75 stroke, round caps) at 1em, inheriting text colour.

## Components

### Buttons
Solid and printed; the edition decides the colour.
- **Shape:** 4px radius, 10px by 18px padding, 700 weight, 1px border matching the fill.
- **Primary:** edition fill with its on-edition text; near-black with white text where no user is in view.
- **On the band:** inverted to white fill with edition-coloured text so it stands on the edition ground.
- **Hover / Press:** soft hover shadow (0.2s); press nudges 1px down and drops the shadow (0.15s). Disabled shows 0.75 opacity with a progress cursor.
- **Loading:** slow forms (the OMDb lookup) disable the submit button, swap its text for a message ending in a real ellipsis, and show a 0.9em ring spinner.
- **Quiet:** white fill, ink text, hairline border that darkens to ink on hover. Inside the rename form it becomes an underlined text button that turns edition-coloured on hover.
- **Danger:** underlined `err` text with no fill or horizontal padding; darkens on hover. Destructive actions confirm first.

### Inputs / Fields
- **Style:** white, 1px hairline border, 4px radius, 10px by 12px padding, inherits body type; caret in the edition colour. Placeholders are short and grey.
- **Hover:** border darkens to soft ink (0.2s).
- **On the band:** the border disappears; the white field on the edition ground is the shape.
- **Inline edit (rename):** the film title is itself the input, 700 at 1.15rem, borderless and transparent at rest; on hover or focus it gains the hairline border, white fill and 12px left padding. Its label is visually hidden.

### Notices
Flash messages under the band or head: tinted full-width strips, 4px radius, 10px by 14px padding, 500 weight, success in green on mint and errors in red on pink, announced as status.

### Navigation
A top bar with the logo (four leaning spines on a plank, in teal, cobalt, mustard and coral) and the uppercase wordmark on the left, text links on the right. Links are 500 weight ink without underline; hover and the current page show a 2px ink underline bar. A skip link appears at the top left on focus.

### User Spine (signature)
A link shaped as a book spine in the user's edition colour: name in vertical uppercase spine lettering, a hairline rule in the soft edition ink, then the edition number (`Nº 01`) and the film count. On hover or focus it rises 18px off the plank with the lifted shadow (0.35s, ease-out `cubic-bezier(0.16, 1, 0.3, 1)`).

### Edition Band
The page head of a user's list: full-bleed edition colour with a back link (SVG arrow plus text), the display heading, the edition number and film count, and the add-movie form.

### Edition Cover (signature)
A cover with its spine strip: the strip is a 34px edition-coloured column with the title in vertical capitals and the number at its foot (`Nº 001`, film order by id). Without a poster, the cover becomes a `wall-deep` field with the title in spine lettering. On hover or focus within the card, the cover slides 10px right and tilts 1.2 degrees from its left edge, gaining the pulled shadow (0.45s, same ease-out). Below sit the inline rename row, a Year/Director fact list (missing values read "unknown") and the Delete text button.

### Empty Shelf
A short soft-ink sentence above a 14px plank, telling the visitor the first action.

## Do's and Don'ts

### Do:
- **Do** give every user exactly one edition colour from the eight, by `user.id % 8`, and let that colour paint their spine, band, cover spines and primary actions.
- **Do** set spine and heading text in Big Shoulders Display, uppercase, and every edition number and count with tabular numerals and the `Nº` prefix.
- **Do** stand spines and covers on a dark plank, continuous across each row.
- **Do** keep lift as a hover/focus response: spines rise 18px, covers slide 10px out from their spine; all motion uses the `cubic-bezier(0.16, 1, 0.3, 1)` ease-out and stops under reduced motion.
- **Do** draw icons as inline SVG line art that inherits text colour.
- **Do** pair each edition with a text colour that keeps at least 4.5:1, including the soft secondary ink.

### Don't:
- **Don't** use a dark page ground or a black-and-red streaming palette; near-black is ink and plank, never the room.
- **Don't** use saturated colour on chrome, panels or page grounds that do not belong to a user.
- **Don't** add inset strips, bevels or gradients to spines; spines are flat colour.
- **Don't** use Unicode arrows or glyph characters as icons.
- **Don't** set forms, buttons or running text in the condensed display face.
- **Don't** wrap the users shelf into a grid; it is one scrolling row.
- **Don't** rely on an edition-coloured focus ring where the ground is the same edition colour; inside the band the ring switches to `on-edition` so it contrasts with what it sits on.
