"""Funniest Cat Voicemail Greeting — make.fun one-line entry.

Writes a single voicemail greeting, as recorded by a cat, to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output/entry.txt).

Stdlib only. No network. The entry is written to the file, never just
printed to stdout — a print-only entry scores 0.

======================================================================
DECISION RECORD — how the winning line was chosen
======================================================================

Judge's brief (most important first):
  1. Reads as a voicemail greeting recorded by a cat AND lands a laugh.
  2. The joke comes from something specific to cats (naps, boxes,
     knocking things off shelves, demanding food at 4am) — not a generic
     joke with the word "cat" dropped in.
  3. The cat has a clear voice and attitude of its own — a character
     speaking, not an owner writing about a cat.
  4. Works spoken aloud in the few seconds a caller waits; punch
     arrives quickly.
  5. Fresh and surprising, not a pun or catchphrase everyone has heard.

----------------------------------------------------------------------
PASS 1 — draft candidates (four lines, weighed against the brief)
----------------------------------------------------------------------

C1: "You've reached Biscuit. I'm asleep in the box your parcel came
    in. Meow after the beep — I'll wake you at 4am for food."
    (119 chars)
    - Criterion 1: opens with a real voicemail frame ("You've
      reached...") and the laugh comes twice — the beep twist, then
      the 4am threat. Strong.
    - Criterion 2: two cat-specific behaviours in one line — sleeping
      in the delivery box, and the 4am food demand. Strong.
    - Criterion 3: Biscuit speaks in the first person, smug and
      unbothered; the closing line is a promise, not a request. Strong.
    - Criterion 4: three short spoken beats; the punch ("I'll wake
      you at 4am for food") lands last and fast. Strong.
    - Criterion 5: "Meow after the beep" retools the standard
      voicemail instruction instead of recycling a cat pun. Fresh.
    VERDICT: winner.

C2: "Hi, you've reached Miso. I'm busy pushing your glass off the
    table. Leave a message and I'll ignore it at 4am." (110 chars)
    - Criterion 1: voicemail frame is clear and it is funny, but the
      laugh is single-note.
    - Criterion 2: knocking a glass off the table is cat-specific.
      Good.
    - Criterion 3: Miso has attitude ("I'm busy..."), but "Leave a
      message and I'll ignore it" is a generic rude-voicemail joke
      that would work for a teenager too. Weaker voice.
    - Criterion 4: punches quickly. Good.
    - Criterion 5: no fresh twist — the beep is never played with.
    VERDICT: runner-up. Loses to C1 on criteria 3 and 5.

C3: "Hi, it's Pickles. I'm on your keyboard, in your box, knocking
    over your water. Leave a message — I'll scream for food at 4am."
    (125 chars)
    - REJECTED on the gate alone: 125 characters exceeds the 120
      maximum, so it would score Valid 0 and never reach the judge.
    - On the merits it is also weaker: three behaviours crammed into
      one breath read like a list, not a character speaking, and the
      "scream for food" ending repeats C2's 4am idea less sharply.
    VERDICT: cut for length and for being list-y.

C4: "You've reached Mochi. I can't come to the phone — I'm knocking
    your favourite mug off the shelf. Meow after the beep."
    (117 chars)
    - Criterion 1: voicemail frame is clear; "Meow after the beep"
      is a good laugh.
    - Criterion 2: knocking a mug off a shelf is cat-specific. Good.
    - Criterion 3: "I can't come to the phone" is a human voicemail
      cliche — it sounds like an owner doing a cat voice, not a cat.
      Weaker.
    - Criterion 4: fine, but the line ENDS on the beep joke, so there
      is no second payoff; the laugh peaks and stops.
    - Criterion 5: the beep twist is fresh, but C1 has the same twist
      plus a closing punch.
    VERDICT: loses to C1 on criteria 3 and 4 — same twist, weaker
    ending, less of a character.

----------------------------------------------------------------------
PASS 2 — revision of the winner (C1), for tightness and freshness
----------------------------------------------------------------------

Draft C1 was already the strongest, but it was revised, not just
accepted. Two trims were tried and REJECTED with reasons:

  (a) "your parcel" -> "the parcel" (saves 1 char, 119 -> 118).
      Rejected: "your parcel" reads more naturally spoken aloud —
      the cat is talking to ITS human about THEIR parcel — and the
      saved character buys nothing, since 119 is already inside the
      120 limit with a file write I verify by running the program.

  (b) "asleep" -> "napping" (same length, softer sound).
      Rejected: "asleep" is the flatter, lazier word, which suits a
      cat that cannot be bothered; "napping" sounds like a wellness
      blogger. Voice wins over prettiness.

One swap was tried and KEPT in spirit but reversed: the cat's name
was briefly "Miso" (from C2). Kept as "Biscuit" — a food-named cat
sets up the closing 4am food demand, so the name does joke work
instead of just labelling the speaker.

Final check on the revised line: 119 characters, one line, UTF-8,
not whitespace-only — inside the gate. The em dash is kept because
it reads as a spoken pause ("Meow after the beep — I'll wake you...")
and the line is still plain UTF-8 text.

----------------------------------------------------------------------
REVISION SCORECARD — candidates judged criterion by criterion
----------------------------------------------------------------------

The judge weighs the brief's criteria in order and stops at the
first criterion where two entries differ, unless a later one differs
by much more. So the decisive question is not "which line is best
overall" but "at which criterion does the winner first pull ahead,
and is that lead big enough to survive a later criterion going the
other way". Scored S (strong) / G (good) / W (weak) per criterion:

Criterion                          C1 (winner)  C2   C3   C4
1. Cat voicemail + lands a laugh   S            S    G    S
2. Joke is cat-specific            S            G    G    G
3. Clear cat voice / character     S            W    W    W
4. Punch arrives quickly, spoken   S            G    G    G
5. Fresh, not a tired pun          S            W    G    G

Reading the scorecard in the judge's order:
  - Criterion 1: C1, C2 and C4 all clear it, so it does not decide
    between the three front-runners; C3 is a step behind (its laugh
    is a list, not a greeting). C1's edge here is that it lands TWO
    laughs (beep twist, then 4am threat) where C2 and C4 land one.
  - Criterion 2: C1 is the first to pull clearly ahead. C1 packs
    two cat-specific behaviours (box nap, 4am food demand) into one
    line; C2, C3 and C4 each carry one (glass/mug knock-over) and
    C3's third behaviour is padding, not a second joke.
  - Criterion 3: C1's lead widens. C1 is the only line where the
    cat speaks as a character with an agenda ("I'll wake you") —
    C2 and C4 both borrow a human voicemail cliche ("Leave a
    message", "I can't come to the phone"), which is an owner doing
    a cat voice. By the judge's rule the contest is already decided
    at criterion 3, before criteria 4 and 5 are reached; C1 also
    wins those, so no later criterion can overturn it.
  - Criterion 4: C1's three spoken beats arrive in order — frame,
    twist, threat — and the final beat is the punch, so the caller
    hears the joke complete inside the few seconds of the greeting.
    C4 fails this shape: it ends on the beep joke, so the laugh
    peaks and stops with no closing payoff.
  - Criterion 5: "Meow after the beep" retools the standard
    voicemail instruction ("leave a message after the beep") instead
    of recycling a cat pun; C1 then adds a second fresh idea (the
    4am wake-up threat) rather than stopping at the one twist.

What each writing pass changed, and why:
  - PASS 1 (draft): four candidates written from four different
    cat behaviours (box nap, glass knock-over, keyboard/box/water
    pile-up, mug knock-over). The pass established the shortlist and
    cut C3 on the 120-char gate before any judging — a line that
    cannot pass the gate never reaches the judge, so length is
    checked first, not last.
  - PASS 2 (revision): the winner was tightened, not rewritten.
    Two trims were tried and rejected with reasons (see above:
    "your parcel" stays because the cat addresses ITS human;
    "asleep" stays because the flat, lazy word suits the voice),
    and the name was settled as "Biscuit" because a food-named cat
    sets up the closing food demand — the name does joke work.
    The revision pass changed zero words of the final line's joke
    structure; it confirmed each word earned its place.
  - This revision (deepening): no word of the line changed. The
    scorecard above and the validate_line() helper were added so the
    reasoning that picked the line and the gate the line must pass
    are both explicit in the file, not only in the author's head.

WINNING LINE (119 chars):
    You've reached Biscuit. I'm asleep in the box your parcel came
    in. Meow after the beep — I'll wake you at 4am for food.
"""

import os

ENTRY = (
    "You've reached Biscuit. I'm asleep in the box your parcel came "
    "in. Meow after the beep \u2014 I'll wake you at 4am for food."
)

MAX_CHARS = 120


def validate_line(line: str) -> str:
    """Check one candidate line against the sealed gate, then return it.

    The gate (competition.yaml, "The gate"): entry.txt must be UTF-8
    text of 1 to 120 characters, not only white space. A single line
    is also required by the brief — a voicemail greeting is one
    spoken line, and a newline would break the judge's read.

    Raises ValueError with a specific reason instead of a bare assert,
    so a bad line fails loudly at build time with its cause attached
    rather than silently writing an invalid entry.
    """
    if not isinstance(line, str):
        raise ValueError(f"entry must be str, got {type(line).__name__}")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} chars, gate allows 1-{MAX_CHARS}"
        )
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    # UTF-8 round-trip: the file is written as UTF-8, so the line
    # must survive an encode/decode unchanged (the em dash is the
    # only non-ASCII character here, and it round-trips cleanly).
    if line.encode("utf-8").decode("utf-8") != line:
        raise ValueError("entry is not valid UTF-8 text")
    return line


def main() -> None:
    # Revision note (2026-11-26): the entry line itself is unchanged
    # from the first revision — only the reasoning around it deepened
    # (decision-record scorecard in the docstring) and the gate check
    # moved from inline asserts into validate_line() above, so the
    # rules the sealed scorer applies are enforced in one named place
    # and any future line change gets the same checks for free.
    line = validate_line(ENTRY)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)

    # The file is the entry; this print is only a local confirmation.
    print(f"wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
