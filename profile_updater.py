import json
from datetime import datetime
from ai_client import ask_ai


def update_profile(profile, session_history, subject):

    prompt = f"""
You are the profile manager for an AI Study Companion.

You have:

1. The student's existing JSON profile.
2. A completed study session.

Your job is to update the student's profile based ONLY
on evidence from the study session.

IMPORTANT RULES:

- Return ONLY valid JSON.
- Keep the existing structure.
- Do not delete useful existing information.
- Do not replace a strength with a weakness because of
  one mistake.
- Do not invent information.
- Add new strengths only when supported by evidence.
- Add weaknesses only when supported by repeated or
  meaningful evidence.
- Update avg_accuracy when the session provides evidence
  that can reasonably affect it.
- Increase sessions_count by 1.
- Update last_session.
- Add the completed session to Chat_History.
- Update learning style only when there is evidence.
- Preserve existing information that is still valid.

EXISTING PROFILE:

{json.dumps(profile, indent=2)}

COMPLETED SESSION:

{json.dumps(session_history, indent=2)}

SUBJECT:

{subject}

Today's date:

{datetime.now().strftime("%Y-%m-%d")}

Return the complete updated student profile as JSON.
"""

    response = ask_ai(prompt)

    return json.loads(response)
