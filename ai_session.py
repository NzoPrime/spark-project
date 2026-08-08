from ai_client import ask_ai


def run_session(profile, subject):

    history = []

    system_context = f"""
You are an AI Study Companion.

Student:
{profile["student"]}

Grade:
{profile["Grade"]}

Learning style:
{profile["Personal_Info"]["lerning_style"]}

Ambition:
{profile["Personal_Info"]["ambition"]}

Subject:
{subject}

Student profile:
{profile}

Your job is to help the student learn.

Adapt your teaching based on the profile.

Do NOT make every interaction a quiz.

If the student struggles:
- explain the concept
- use simpler language
- give examples
- ask a smaller follow-up question

If the student understands:
- increase the difficulty gradually
- explore the topic deeper

Remember that one mistake does not automatically mean
the student is weak at a topic.

Keep the conversation suitable for Grade {profile["Grade"]}.
"""

    first_prompt = system_context + """

Start the study session.
Greet the student and begin studying the selected subject.
"""

    ai_message = ask_ai(first_prompt)

    print("\nAI:", ai_message)

    history.append({
        "role": "assistant",
        "content": ai_message
    })

    while True:

        student_message = input("\nYou: ")

        if student_message.lower() in [
            "exit",
            "quit",
            "end",
            "finish"
        ]:
            break

        history.append({
            "role": "student",
            "content": student_message
        })

        conversation = system_context + "\n\nConversation:\n"

        for message in history:
            conversation += (
                f'{message["role"]}: '
                f'{message["content"]}\n'
            )

        conversation += """
Continue the study session.

Respond naturally to the student's latest message.
"""

        ai_message = ask_ai(conversation)

        print("\nAI:", ai_message)

        history.append({
            "role": "assistant",
            "content": ai_message
        })

    return history
