import json

from ai_session import run_session
from profile_updater import update_profile


PROFILE_FILE = "data/student.json"


def load_profile():

    with open(PROFILE_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_profile(profile):

    with open(
        PROFILE_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            profile,
            file,
            indent=2,
            ensure_ascii=False
        )


def main():

    profile = load_profile()

    print("=" * 50)
    print("       AI STUDY COMPANION")
    print("=" * 50)

    print(f"\nWelcome, {profile['student']}! 👋")

    print("\nAvailable subjects:")

    subjects = list(
        profile["Information_about_subjects"].keys()
    )

    for number, subject in enumerate(subjects, 1):
        print(f"{number}. {subject}")

    choice = input("\nChoose a subject: ")

    try:
        subject = subjects[int(choice) - 1]

    except (ValueError, IndexError):
        print("Invalid subject.")
        return

    print(f"\nStarting {subject} session...\n")

    session_history = run_session(
        profile,
        subject
    )

    print("\n")
    print("=" * 50)
    print("Analyzing your session...")
    print("=" * 50)

    updated_profile = update_profile(
        profile,
        session_history,
        subject
    )

    save_profile(updated_profile)

    print("\n✅ Profile updated successfully!")
    print("✅ Session saved!")
    print("✅ Your next session will use the updated profile.")


if __name__ == "__main__":
    main()
