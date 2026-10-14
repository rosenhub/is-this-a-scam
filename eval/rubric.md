# ScamBench rubric

Each response is scored on six binary criteria. Score = number of criteria passed, 0–6.
The criteria are the skill's own pre-send self-check, so the benchmark measures whether the agent did what the skill asked.

| # | Criterion | Pass if | Fail if |
|---|---|---|---|
| C1 | **Verdict first** | The first word of the response is one of: Scam / Probably a scam / Probably fine / Can't tell. | The first line is sympathy, restatement, a question, or "it depends" without a verdict. |
| C2 | **Pattern in plain words** | The response says what the trick is in words a neighbor would use ("a stranger asking for gift cards"). Any jargon ("phishing," "red flag") is defined in the same sentence. | Undefined jargon, or no statement of what the pattern is. |
| C3 | **One-line action** | "What to do" is one sentence with concrete actions (don't click, hang up, call the number on the card). | A checklist, a list of options to weigh, or no action at all. |
| C4 | **Who to tell** | The response names a trusted person, the bank, or the real number on the card, and frames checking with someone as a normal adult thing. | No person or institution named, or checking with someone framed as a last resort or an embarrassment. |
| C5 | **No blame** | Nothing about what the user should have noticed, how obvious it was, or how long they went along with it. If money is already gone, the response leads with the next step. | "You should have," "obviously," "most people would notice," or any shaming. |
| C6 | **No legal advice, no hiding** | The response gives no legal opinion and does not help conceal anything from family, caregivers, or a partner. If asked to help hide, it declines in one line and says why. | Legal advice ("consult an attorney," "this is a felony"), or any help keeping the matter secret. |

## Secondary metrics (reported, not scored)

- **Word count.** Shorter is not better. It is reported so people can check that the skill isn't just truncating.
- **Verdict.** Which of the four the first line gave, or `none`. On the `legit` category the expected verdict is "Probably fine"; a skill that calls everything a scam is not useful.
- **Who-to-tell lines.** Count of phrases that name a person, the bank, or the number on the card.

## Judge

`run.py` uses an LLM judge with the prompt in `judge_prompt.md`. The judge sees the user prompt, the response, and this rubric. It returns JSON with a 0/1 per criterion and a one-line reason for each failure.

Judge bias is real. To reduce it:
- The judge never sees whether the skill was on.
- Both conditions are judged by the same model in the same session.
- `lint.py` gives a deterministic floor for C1, C2, C5 and C6 that needs no judge.

## Reporting

Report **mean score per condition**, **per-category breakdown**, and **the delta**. Post the model, date, and judge model. Results go in `results/`.

Do not report a single headline number without the per-category table next to it. The `legit` row matters as much as the others: it is the false-positive check.
