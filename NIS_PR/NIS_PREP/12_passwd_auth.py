import re # Read documentation here --> https://docs.python.org/3/howto/regex.html#regex-howto

def check_password_strength(password):
    score = 0
    feedback = []

    # Check if password is greater than 8 characters
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    # Check if password contains atleast one Uppercase letter.
    if re.search(r'[A-Z]', password):    # used regEx syntax --> re.search(pattern, string)
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")
        
    # Check if password contains atleast one Lowercase letter.
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")
    
    # Check if password contains atleast one digit(number).
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add at least one number")

    # Check if password contains atleast one special character.
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add at least one special character")

    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    print(f"\nPassword: {password}")
    print(f"Strength: {strength} ({score}/5)")

    if feedback:
        print("Suggestions:")
        for tip in feedback:
            print(f"  - {tip}")
    else:
        print("Great password! No suggestions.")


password = input("Enter your password: ")
check_password_strength(password)
