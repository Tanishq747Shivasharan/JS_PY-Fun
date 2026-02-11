import string

def check_password_strength(passwd):
    score = 0
    sugg = []

    if len(passwd) >= 8:
        score += 1
    else:
        sugg.append("Make password at least 8 characters long")

    if any(char.isupper() for char in passwd):
        score += 1
    else:
        sugg.append("Add at least one uppercase letter")

    if any(char.isdigit() for char in passwd):
        score += 1
    else:
        sugg.append("Include at least one number")

    if any(char in string.punctuation for char in passwd):
        score += 1
    else:
        sugg.append("Include at least one number")

    if any(char in string.punctuation for char in passwd):
        score += 1
    else:
        sugg.append("Add at least one number")

    if any(char in string.punctuation for char in passwd):
        score += 1
    else:
        sugg.append("Add at least one special symbol {!@#$ etc.}")

        # Strength Rating
    if score == 4:
        strength = "Very Strong"
    elif score == 3:
        strength = "Strong"
    elif score == 2:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, sugg

passwd = input("Enter your password: ")

strength, sugge = check_password_strength(passwd)
print("\nPassword Strength:", strength)

if sugge:
    print("Suggestions to improve:")
    for s in sugge:
        print("-", s)
else:
    print("No suggestions. Great password!")