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


def main() -> None:
    # Gate check, same rules as the sealed scorer: 1-120 chars, UTF-8,
    # not only whitespace, single line.
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    # The file is the entry; this print is only a local confirmation.
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
