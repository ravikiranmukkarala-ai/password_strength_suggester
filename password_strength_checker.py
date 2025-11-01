# password_strength_suggester.py
# A simple Python script that checks password strength
# and suggests stronger passwords based on user input.

import re
import random
import string

def check_password_strength(password):
    """Returns a strength score and feedback for the given password."""
    strength = 0
    feedback = []

    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        feedback.append("❌ Password too short. Use at least 12 characters.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("❌ Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("❌ Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("❌ Add at least one number.")

    if re.search(r"[@$!%*?&^#_+-]", password):
        strength += 1
    else:
        feedback.append("❌ Add at least one special character (@, #, $, etc.).")

    if strength >= 6:
        status = "✅ Very Strong"
    elif strength >= 4:
        status = "🟩 Strong"
    elif strength >= 3:
        status = "🟨 Moderate"
    else:
        status = "🟥 Weak"

    return status, feedback


def suggest_stronger_password(password):
    """Suggests a stronger version of the user's password."""
    # Add missing character types based on input
    new_password = password

    if not re.search(r"[A-Z]", new_password):
        new_password += random.choice(string.ascii_uppercase)

    if not re.search(r"[a-z]", new_password):
        new_password += random.choice(string.ascii_lowercase)

    if not re.search(r"[0-9]", new_password):
        new_password += random.choice(string.digits)

    if not re.search(r"[@$!%*?&^#_+-]", new_password):
        new_password += random.choice("@$!%*?&^#_+-")

    # Ensure password is at least 12 chars
    while len(new_password) < 12:
        new_password += random.choice(string.ascii_letters + string.digits)

    return new_password


if __name__ == "__main__":
    print("🔐 Password Strength Checker with Suggestions")
    user_password = input("Enter a password: ")

    result, suggestions = check_password_strength(user_password)

    print("\nPassword Strength:", result)
    if suggestions:
        print("\nSuggestions to improve:")
        for tip in suggestions:
            print("  -", tip)

        stronger = suggest_stronger_password(user_password)
        print(f"\n💡 Suggested stronger password: {stronger}")
    else:
        print("Your password looks great! 🔥")
