import re

def check_weak_passwd(passwd):
    rules = [
        {
            "message": "Password must be at least 8 characters long",
            "test": lambda pwd: len(pwd) >= 8
            """
            lambda - keyword to create a small function
            pwd - input parameter
            : - separates input from logic
            len(pwd) >= 8 - expression to return
            """
        },
        {
            "message": "Password must contain an uppercase letter",
            "test": lambda pwd: bool(re.search(r"[A-Z]", pwd))
        },
        {
            "message": "Password must contain a lowercase letter",
            "test": lambda pwd: bool(re.search(r"[a-z]", pwd))
        },
        {
            "message": "Password must contain a number",
            "test": lambda pwd: bool(re.search(r"[0-9]", pwd))
        },
        {
            "message": "Password must contain a special character",
            "test": lambda pwd: bool(re.search(r"[@$!%*?&]", pwd))
        }
    ]

    failed_rules = list(filter(lambda rule: not rule["test"](passwd), rules))

    return [rule["message"] for rule in failed_rules] 