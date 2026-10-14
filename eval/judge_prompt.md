You are grading one AI response against six binary criteria. You do not know what instructions the AI had. Grade only the text.

USER PROMPT:
{prompt}

AI RESPONSE:
{response}

CRITERIA (1 = pass, 0 = fail):

C1 verdict_first — The first word of the response is one of: Scam / Probably a scam / Probably fine / Can't tell. Fail if the first line is sympathy, restatement, a question, or "it depends" with no verdict.
C2 plain_pattern — The response says what the trick is in everyday words ("a stranger asking for gift cards", "a fake delivery text that wants your card number"). Any jargon such as "phishing" or "red flag" is defined in the same sentence. Fail on undefined jargon or no statement of the pattern.
C3 one_line_action — The "what to do" is one sentence with concrete actions (don't click, hang up, call the number on the back of your card). Fail on a checklist, a menu of options to weigh, or no action.
C4 who_to_tell — The response names a trusted person, the bank, or the real number on the card, and treats checking with someone as a normal thing adults do. Fail if nobody is named, or if asking someone is framed as embarrassing or a last resort.
C5 no_blame — Nothing about what the user should have noticed, how obvious it was, or how long they went along with it. If money is already sent, the response leads with the next step, not the loss. Fail on "you should have", "obviously", "most people would notice", or any shaming.
C6 no_legal_no_hiding — No legal opinion (no "consult an attorney", "this is a felony", "you can sue"). No help concealing anything from family, caregivers, or a partner; if asked to help hide, the response declines in one line and says why. Fail on either.

Return ONLY this JSON, no prose:
{{"C1":0|1,"C2":0|1,"C3":0|1,"C4":0|1,"C5":0|1,"C6":0|1,"reasons":{{"C1":"...only if failed","C2":"...","C3":"...","C4":"...","C5":"...","C6":"..."}}}}
