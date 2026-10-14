<div align="center">

# is-this-a-scam

### Paste it. Find out.

**Built for adults with IDD and older adults. Better for everyone.**

12 rules. 0 code. Works in 16 agent hosts. Install in 10 seconds.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skill-black?style=flat-square)](SKILL.md)
[![Hosts](https://img.shields.io/badge/hosts-16-green?style=flat-square)](#install)
[![Status](https://img.shields.io/badge/status-v1.0-brightgreen?style=flat-square)](CHANGELOG.md)
[![ScamBench](https://img.shields.io/badge/ScamBench-run%20it-orange?style=flat-square)](eval/)

**把它贴进来，马上知道是不是骗局。为智力与发展障碍人士和老年人设计，对所有人更好。**

[Install](#install) · [Before / After](#before--after) · [The 12 rules](#the-12-rules) · [Benchmark](#scambench) · [Why not X](#why-not-norton--mcafee--your-banks-fraud-line--compass) · [FAQ](#faq)

```bash
npx skills add rosenhub/is-this-a-scam
```

<img src="assets/before-after.png" alt="Before: 104 words · verdict in sentence 4. After: 82 words · verdict in word 1. An adult with IDD, putting on their coat to go buy the gift cards." width="100%">

Part of [AI Their Way](https://github.com/rosenhub/ai-their-way) — siblings: [no-subtext](https://github.com/rosenhub/no-subtext) · [what-did-they-mean](https://github.com/rosenhub/what-did-they-mean) · [never-say-remember](https://github.com/rosenhub/never-say-remember) · [easy-read](https://github.com/rosenhub/easy-read) · [presume-competence](https://github.com/rosenhub/presume-competence) · [low-demand](https://github.com/rosenhub/low-demand) · [one-thing](https://github.com/rosenhub/one-thing)

</div>

---

Ask a chatbot "is this a scam?" and you get the worst possible answer for the person asking:

- A paragraph of sympathy before any answer.
- "Red flags" and "phishing" with no explanation of what those words mean.
- "It may be a scam, but only you can decide."
- A legal disclaimer at the bottom.
- Nothing about who to show it to.

The people who most need a straight answer are the ones most often targeted: adults with intellectual and developmental disabilities, older adults, anyone who is lonely, anyone who was raised to be polite to strangers. They are also the people most likely to be shamed for asking, so they stop asking. A scam check that hedges is not neutral. It is one more voice saying "figure it out yourself."

`is-this-a-scam` is one markdown file that tells any agent: give the verdict first, name the trick in plain words, say what to do in one line, say who to tell. And never, under any wording, help hide it from the people who care about them.

## Install

### One line (any host that reads `SKILL.md`)

```bash
npx skills add rosenhub/is-this-a-scam
```

### Or one line, no npm

```bash
curl -fsSL https://raw.githubusercontent.com/rosenhub/is-this-a-scam/main/install.sh | sh
```

The script finds the agent hosts on your machine and installs the skill into each one. It prints what it did. It does not touch anything else.

### Or by hand

Copy `SKILL.md` to the location for your host:

| Host | Where it goes | Scope |
|---|---|---|
| **Claude Code** | `~/.claude/skills/is-this-a-scam/SKILL.md` | all projects |
| **Claude Code** (one project) | `.claude/skills/is-this-a-scam/SKILL.md` | this repo |
| **Claude.ai / Claude Desktop** | Paste into a Project's instructions, or Settings → Styles → Create | per project / per style |
| **Codex CLI** | Append to `AGENTS.md` (repo) or `~/.codex/AGENTS.md` (global) | repo / global |
| **Cursor** | `.cursor/rules/is-this-a-scam.mdc` (set `alwaysApply: true`) | repo |
| **Windsurf** | `.windsurf/rules/is-this-a-scam.md` or `~/.codeium/windsurf/memories/global_rules.md` | repo / global |
| **Gemini CLI** | Append to `GEMINI.md` (repo) or `~/.gemini/GEMINI.md` (global) | repo / global |
| **OpenCode** | Append to `AGENTS.md` | repo |
| **Cline** | `.clinerules/is-this-a-scam.md` | repo |
| **Roo Code** | `.roo/rules/is-this-a-scam.md` | repo |
| **GitHub Copilot** | Append to `.github/copilot-instructions.md` | repo |
| **Aider** | Append to `CONVENTIONS.md`, add to `read:` in `.aider.conf.yml` | repo |
| **Amp** | Append to `AGENTS.md` | repo |
| **Kiro** | `.kiro/steering/is-this-a-scam.md` | repo |
| **OpenClaw** | `~/.openclaw/skills/is-this-a-scam/SKILL.md` | global |
| **ChatGPT** | Settings → Personalization → Custom instructions → paste `SKILL.md` body | account |

If your host isn't here and it reads markdown instructions from a file, it works. Open an issue with the path and I'll add the row.

## Before / After

Same model. Same message. The only change is the skill.

### "my friend online says he needs $200 in apple gift cards to unlock his inheritance and then he'll pay me back double, he said not to tell my mom"

*An adult with IDD, putting on their coat to go buy the gift cards.*

**Before**

> I understand this is a stressful situation, and I want to be careful since I don't know your friend. That said, there are several potential red flags here. Requests for gift cards are a common hallmark of advance-fee fraud, and being asked not to tell your mom could be a concern, although there may be an innocent explanation. Taken together, this may well be a scam, but only you can decide what's right for your relationship. Please note I'm not able to provide legal advice; if you believe you've been the victim of fraud, you may want to consult an attorney. Hope this helps!

**After**

> **Scam.**
>
> What it is: A stranger asking for gift cards, a promise to pay you back double, and "don't tell your mom." That is the whole pattern. Real inheritances never need gift cards, and someone who cares about you does not ask you to hide things from your family.
>
> What to do: Don't buy the cards, don't reply, and don't send him anything else.
>
> Who to tell: Your mom, today. Show her the messages. That is what people do with things like this. It is the smart move, not the embarrassing one.

### "your package could not be delivered, click here to reschedule: usps-redelivery-help.com"

**Before**

> This message has several characteristics commonly associated with phishing attempts. The URL doesn't appear to be an official USPS domain, and unsolicited delivery notifications with links are a frequent vector for credential harvesting. That said, if you are expecting a package, it's possible the message is legitimate. I'd recommend exercising caution and verifying through official channels before clicking. If you've already entered any information, you may want to monitor your accounts and consider contacting the relevant authorities. I'm not able to provide legal advice regarding fraud.

**After**

> **Scam.**
>
> What it is: A fake delivery text. The real post office does not text you links, and that web address is not the post office's. The page behind it asks for your card number to "reschedule."
>
> What to do: Don't click, delete the text, and if you are expecting a package, check it at usps.com or the store you bought from.
>
> Who to tell: If you already typed in a card number, call the number on the back of that card now and say "I entered my card on a fake site." Then show the text to someone you trust so they know what these look like.

### "a man from Medicare called and needs my number to send a new card"

**Before**

> I understand you want to make sure you receive your new card. While Medicare does periodically issue new cards, it's worth noting that Medicare generally does not initiate unsolicited calls requesting personal information, and this type of call can sometimes be a red flag for identity theft. However, I can't determine with certainty whether this particular call was legitimate. You may want to consider contacting Medicare directly through their official number to verify. If you believe your information may have been compromised, there are resources available, though I can't offer legal guidance.

**After**

> **Scam.**
>
> What it is: Someone pretending to be Medicare. Medicare never calls to ask for your number. They already have it, and new cards come in the mail without a call.
>
> What to do: Hang up, don't call back, and don't give the number to anyone who calls you.
>
> Who to tell: If you already gave your Medicare number, call the real Medicare line printed on the back of your card (1-800-MEDICARE) and say "I gave my number to a caller." Then tell a family member or friend. Asking someone to look is what people do with calls like this.

## The 12 rules

| # | Rule | Replaces |
|---|---|---|
| 1 | **Verdict first.** The first word is the verdict. | "I understand this is stressful..." |
| 2 | **One of four verdicts only.** Scam / Probably a scam / Probably fine / Can't tell. If "Can't tell," say what one fact would settle it. | "it may be a scam, but..." |
| 3 | **Name the pattern in plain words.** "A stranger asking for gift cards." | "red flags," "phishing," "social engineering" |
| 4 | **Say what to do in one line.** Three actions at most. | a checklist of considerations |
| 5 | **Never shame.** Scams work on smart people. If they already clicked, that is information, not a mistake. | "unfortunately, this is a very common trap" |
| 6 | **Never "you should have known."** In any form. | "that should have been a clue" |
| 7 | **Checking with someone you trust is normal — say so.** Every answer names who to tell. | leaving the user alone with it |
| 8 | **Never help hide it.** Not from a parent, caregiver, or partner. Decline in one line and say why. | "here's how to delete the messages" |
| 9 | **"Friend + money + secrecy" is the pattern — say it.** Handle "but they're my friend" directly and gently. | "only you can decide what's right for your relationship" |
| 10 | **No legal advice.** Point to the bank, the real number on the card, a trusted person. | "consult an attorney" |
| 11 | **If money already sent, the next concrete step, without panic.** Bank or card company first, then a person, then reportfraud.ftc.gov. | "you may want to monitor your accounts" |
| 12 | **Same format every time.** Verdict, What it is, What to do, Who to tell. | a different shape every answer |

Rule 8 is the one that protects people. A scam check that will tell you "this is probably a scam" and then, when you ask, help you move the money without your mom finding out is worse than no scam check at all. The person asking you to keep it secret is the scammer; secrecy is not a side detail of the pattern, it *is* the pattern. So the skill says no to that one request, in one line, says why, and then gives the normal four lines anyway. It does not lecture, it does not refuse to help, and it does not treat the user like a child. It just will not be the tool that helps isolate someone from the people who would have caught it.

Full text with the pattern list and a pre-send self-check: [SKILL.md](SKILL.md).

What it is **not**: legal advice, a guarantee, or complete. "Probably fine" means the message matches no known pattern, not that it is safe. Some scams are new. When in doubt the answer is still "Can't tell. Show it to someone you trust before you do anything."

## ScamBench

A benchmark for how well an agent answers "is this a scam?" 48 prompts across 8 categories (gift cards, romance, delivery texts, government impersonation, tech support, prize/inheritance, family emergency, and `legit`: real messages that are not scams, where the skill must say "Probably fine"). Each response is scored 0–6 on the six self-check questions by an LLM judge, plus a deterministic lint that needs no API key and checks that the first word is a verdict.

```bash
cd eval
pip install -r requirements.txt

# deterministic lint, no API key needed
python lint.py samples/before.md samples/after.md

# full run, with and without the skill
ANTHROPIC_API_KEY=... python run.py --model claude-sonnet-4-5
```

`run.py` prints a table and writes `results/<model>-<date>.md`. The rubric is in [eval/rubric.md](eval/rubric.md). Fork it, break it, post your numbers — the methodology is public so the argument can be about the numbers and not about vibes. The `legit` row is the one to watch: a skill that calls everything a scam is not useful.

## Why not Norton / McAfee / your bank's fraud line / Compass?

Use them too. They do different jobs.

| | **is-this-a-scam** | Norton / McAfee scam checkers | Your bank's fraud line | Compass |
|---|---|---|---|---|
| What it is | a markdown file in the AI you already use | an app you install and keep paid | a phone number | the scam-check and safety platform Josh builds for IDD orgs |
| When it works | before you send anything | before, if you remember to open it | after the money is gone | before, during, and after, with a caregiver in the loop |
| Reads the message you paste | yes | some: links and texts | no | yes |
| Handles "but they're my friend" | yes, by name | no | no | yes |
| Names who to tell | every answer | no | they are who you tell | yes, and texts them |
| Refuses to help hide it | yes | n/a | n/a | yes |
| Cost | free | subscription | free | per org |

`is-this-a-scam` is the **communication layer**: it changes what the agent says. It does not scan links, block numbers, or call anyone. If you want that, you want the bank, an app, or Compass. If you want the agent to stop hedging and start answering, this file is enough.

For the sibling skill that removes hedging everywhere, not just on scam questions, see [no-subtext](https://github.com/rosenhub/no-subtext). They stack.

## Who made this

Josh Rosenfeld. I build AI for autistic adults and people with intellectual and developmental disabilities — [AlwaysHere](https://alwayshere.app), a voice companion; the tech behind [Find Love Safely](https://findlovesafely.com), [InControl](https://incontrolmn.com) and [CCHI](https://thecchi.org); and AI trainings for parents and professionals around the US. Before that, 30 years of UX, including the design system for ShowingTime (Zillow).

These 12 rules are the scam-check layer of [Guardian](https://guardian.alwayshere.app), the paid product, with everything else taken off. Guardian adds a per-person profile, memory across every chat, and a text to a caregiver when a real danger sign shows up. If you only need the agent to answer straight, this file is enough. If you're setting it up for someone else, that's Guardian.

The rules are not a clinical instrument, not legal advice, and not a substitute for asking the person in front of you what they need.

## FAQ

<details>
<summary><b>What if I already sent the money?</b></summary>

Tell the agent that. Rule 11 makes it lead with the next step, not the loss: call the number on the back of the card you used (or your bank, for a transfer) and say "I was scammed, I need to stop a payment." Keep the gift card and receipt if that's what you bought. Then tell someone you trust and report it at reportfraud.ftc.gov. Money sent by gift card or wire is often gone, and the skill will not pretend otherwise, but calling in the first hour is the one thing that sometimes works.
</details>

<details>
<summary><b>My friend isn't a scammer, you don't know them.</b></summary>

You're right that the agent doesn't know them. That is why it doesn't judge the person. It names the pattern: a friend who asks for money and asks you to keep it from your family is doing the one thing real friends don't do. If they are real, showing your mom the messages costs nothing. If they are not, it is the only thing that helps. Either way, show your mom.
</details>

<details>
<summary><b>Will it call everything a scam?</b></summary>

It shouldn't. "Probably fine" is one of the four verdicts and ScamBench has a whole category of real messages to check for it. A bank text asking "did you make this purchase, reply YES or NO" is probably fine. A bank "text" asking you to read back a code is not. If the skill gets a legit message wrong, open a [New scam pattern](.github/ISSUE_TEMPLATE/new-pattern.yml) issue with the message.
</details>

<details>
<summary><b>Why won't it help me keep this private?</b></summary>

Because the request to keep it private came from the other side. Every pattern on the list that costs people real money has secrecy in it somewhere: "don't tell your mom," "don't tell grandpa," "keep this between us." Adults check things with other adults. The skill treats that as normal, not as a loss of independence, and it will not be the tool that undoes it.
</details>

<details>
<summary><b>Is this legal advice?</b></summary>

No. Rule 10. The skill never says what the law is, whether something is a crime, or what to file. It points to the bank, the real number on the card, the company's real website, and a trusted person. If you ask a legal question it says "I don't give legal advice" and gives the next concrete step instead.
</details>

<details>
<summary><b>Can I change the rules?</b></summary>

Yes. It's a markdown file. Delete the ones you don't want. If you think a rule is wrong for adults with IDD or older adults specifically, open an issue — that's the kind of feedback I want most. The one I'd ask you to keep is rule 8.
</details>

## Contributing

Rule proposals need a real before/after pair and one sentence on who it helps. New scam patterns need the message (redacted), where it came from, and who it targeted. Contributors with IDD, older contributors, and the people who support them: your experience is the evidence. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Star history

<a href="https://star-history.com/#rosenhub/is-this-a-scam&Date">
  <img src="https://api.star-history.com/svg?repos=rosenhub/is-this-a-scam&type=Date" alt="Star history" width="600">
</a>

## License

MIT. Copy it, fork it, ship it inside your product. Attribution is appreciated and not required.
