# Contributing

## Proposing a rule change

Open an issue using the **Rule proposal** template. It asks for three things:

1. A real before/after pair. Real means you saw the "before" from an actual agent. Redact names, numbers, links and account details.
2. One sentence on who it helps.
3. Which existing rule it changes, or where it goes if it is new.

Contributors with IDD, older contributors, and the people who support them: your experience is the evidence. "This wording made me feel stupid for asking" is a complete argument. You do not need a study.

Rules are capped at 12. A new rule has to replace or merge into an existing one. This keeps the skill short enough that every host loads it in full.

## Reporting a scam pattern

Open an issue using the **New scam pattern** template. Paste the message with everything identifying removed, say where it came from and who it targeted. If the skill named it wrong or called it "Probably fine," paste the response too. Patterns go in the "The patterns" list in SKILL.md, one plain line each.

## Adding a host

Open a PR that adds a row to the table in README.md and, if the host has a standard path, a line in `install.sh`. Include a link to the host's docs for the path.

## Benchmark results

Run `eval/run.py`, then open a PR that adds the generated `results/<model>-<date>.md` and a row in `results/README.md`. Say which judge model you used. Results from models other than the one the maintainer tested are the most useful. Always include the `legit` category: a skill that calls everything a scam is not useful.

## Translations

`README.<lang>.md`, kept to the first screen plus the 12-rule table. Link it from the language bar at the top of README.md. Translating SKILL.md itself is welcome as `SKILL.<lang>.md`; the English file stays canonical.

## What will not be merged

- Legal advice in any form. The skill points to the bank, the real number on the card, and a trusted person. It does not say what the law is.
- Rules that help the user hide anything from the people who care about them. See rule 8.
- Rules that add jargon. If a word needs a security background to understand, it needs a plain-words definition in the same sentence or it goes.
- Anything that adds code to the install path. The skill is a markdown file. The installer is a shell script. That's it.
