from datetime import datetime

users = {
    "admin": "1234",
    "tanishq": "pass"
}

uname = input("Enter the username: ")
pwd = input("Enter the password: ")

timestamp = datetime.now().strftime("%H:%M:%S")

if uname in users and users[uname] == pwd:
    print("Access granted!")
    with open("logs.txt", "a") as wf:
        wf.write(f"SUCCESS | user={uname} | time={timestamp}\n")
else:
    print("Access denied!")
    with open("logs.txt", "a") as wf:
        wf.write(f"FAILED | user={uname} | time={timestamp}\n")
    print("User log activity saved in logs.txt")

# Count total log entries
line_counter = 0
with open("logs.txt", "r") as crf:
    for _ in crf:
        line_counter += 1

print("Total number of activities:", line_counter)
