import re

def check_weak_passwd(passwd):
    rules = [
        {
            "message": "Password must be at least 8 characters long",
            "test": lambda pwd: len(pwd) >= 8
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


passwd = input("Enter your password: ")

errs = check_weak_passwd(passwd)
if len(errs) == 0:
    print("Your password is strong enough")  
else:
    print("Your password is weak, please try again")
    print("Your password should contain at least 8 characters, 1 uppercase letter, 1 lowercase letter, 1 number and 1 special character")
    print("Your password should not contain any spaces")
    print("Your password should not contain any common words")
    print("Your password should not contain any common sequences")
    print("Your password should not contain any common patterns")
    print("Your password should not contain any common substrings")
    for err in errs:
        print("-",err)