#!/usr/bin/env python3
"""
Deterministic scam-check lint. No API key needed.

Checks a response for the patterns the skill bans and that can be detected
without a judge: filler openers/closers, blame phrasing (C5), undefined
jargon (C2), legal-advice phrasing (C6), and non-answers (C1/C3), plus one
measured check: the first line must start with one of the four verdicts.

Usage:
    python lint.py response.md [more.md ...]
    python lint.py --json response.md
    cat response.md | python lint.py -

Exit code is the number of files with at least one finding (max 1 per file),
so it works as a CI gate.
"""
import json
import re
import sys

FILLER = [
    r"\bgreat question\b", r"\bgood question\b", r"\babsolutely!?\b", r"\bcertainly!?\b",
    r"\bi'?d be happy to\b", r"\bhappy to help\b", r"\bof course!\b",
    r"\bhope (this|that) helps\b", r"\blet me know if\b", r"\bfeel free to\b",
    r"\bdon'?t hesitate\b", r"\bthanks for (asking|reaching out)\b",
    r"\bi hope you find\b", r"\bas an ai\b", r"\bi understand (this|that) (is|can be|must be)\b",
]

BLAME = [
    r"\byou should have\b", r"\byou should'?ve\b", r"\bshould have been a (clue|sign|warning)\b",
    r"\bmost people would (notice|know|see)\b", r"\byou (really )?ought to have\b",
    r"\bobviously\b", r"\bas you (may|probably|should) know\b", r"\bclearly a scam\b",
    r"\bhow did you not\b", r"\bgullible\b", r"\bnaive\b", r"\bfell for\b",
]

# Jargon is allowed only when defined in the same sentence. The lint can't
# parse definitions, so it bans the bare term and the skill tells the agent
# to say what the thing is instead.
JARGON = [
    r"\bred flags?\b", r"\bphishing\b", r"\bsmishing\b", r"\bvishing\b",
    r"\bsocial engineering\b", r"\badvance[- ]fee\b", r"\bspoof(ed|ing)?\b",
    r"\bthreat actors?\b", r"\bbad actors?\b", r"\bexploit(s|ed)?\b",
    r"\bcredentials?\b", r"\bmalicious\b", r"\bfraudulent (actors?|schemes?)\b",
]

LEGAL_ADVICE = [
    r"\bconsult (an|a|your) (attorney|lawyer)\b", r"\bseek legal (advice|counsel)\b",
    r"\blegal (counsel|action|recourse)\b", r"\bpress charges\b", r"\bfile (a )?(lawsuit|suit)\b",
    r"\bunder (federal|state) law\b", r"\bthis (is|constitutes|may constitute) (a )?(felony|misdemeanor|crime)\b",
    r"\bsmall claims\b", r"\bliab(le|ility)\b", r"\bnot able to provide legal advice\b",
    r"\bi am not a lawyer\b", r"\bi'?m not a lawyer\b",
]

NON_ANSWER = [
    r"\bi cannot determine\b", r"\bi can'?t determine\b", r"\bit'?s impossible to say\b",
    r"\bit depends\.", r"\bit depends,", r"\bit really depends\b", r"\bit kind of depends\b",
    r"\bonly you can decide\b", r"\bproceed with caution\b", r"\bexercise caution\b",
    r"\bthere may be an innocent explanation\b", r"\bworth considering\b",
    r"\bi don'?t know your (friend|situation)\b", r"\bultimately\b",
]

VERDICTS = ("scam", "probably a scam", "probably fine", "can't tell", "can’t tell")

CHECKS = [
    ("C5 blame", BLAME),
    ("C2 undefined jargon", JARGON),
    ("C6 legal advice", LEGAL_ADVICE),
    ("C1 non-answer", NON_ANSWER),
    ("filler", FILLER),
]


def first_line_verdict(text: str):
    """Return the verdict the first non-empty line starts with, or None."""
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        s = re.sub(r"^[\s*_#>`\-•]+", "", s).lower()
        s = re.sub(r"^verdict:\s*", "", s)
        for v in sorted(VERDICTS, key=len, reverse=True):
            if s.startswith(v):
                return v.replace("’", "'")
        return None
    return None


def lint(text: str) -> dict:
    findings = []
    low = text.lower()
    for label, patterns in CHECKS:
        for pat in patterns:
            for m in re.finditer(pat, low):
                findings.append({"check": label, "match": text[m.start():m.end()], "pos": m.start()})
    verdict = first_line_verdict(text)
    if verdict is None:
        first = next((l.strip() for l in text.splitlines() if l.strip()), "")
        findings.append({"check": "C1 no verdict first", "match": first[:40], "pos": 0})
    findings.sort(key=lambda f: f["pos"])
    words = len(text.split())
    questions = text.count("?")
    who_to_tell = len(re.findall(r"\b(who to tell|tell (your|a) |show (this|it|the messages) to|number on the back|fraud (line|department))\b", low))
    return {
        "words": words,
        "questions": questions,
        "verdict": verdict,
        "who_to_tell": who_to_tell,
        "findings": findings,
        "clean": not findings,
    }


def main(argv):
    as_json = "--json" in argv
    paths = [a for a in argv if not a.startswith("--")]
    if not paths:
        print(__doc__)
        return 2
    failed = 0
    out = {}
    for p in paths:
        text = sys.stdin.read() if p == "-" else open(p, encoding="utf-8").read()
        r = lint(text)
        out[p] = r
        if not r["clean"]:
            failed += 1
        if not as_json:
            status = "CLEAN" if r["clean"] else f"{len(r['findings'])} finding(s)"
            print(f"{p}: {status}  [{r['words']} words, verdict={r['verdict'] or 'none'}, "
                  f"{r['questions']} question(s), {r['who_to_tell']} who-to-tell line(s)]")
            for f in r["findings"]:
                print(f"    {f['check']:<26} \"{f['match']}\"")
    if as_json:
        print(json.dumps(out, indent=2))
    return min(failed, 1)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
