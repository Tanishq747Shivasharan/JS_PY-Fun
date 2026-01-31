from datetime import datetime,timezone

# Dictionary based authentication.
users = {
    "admin" : "1234",
    "tanishq": "pass"
}

uname = input("Enter the username: ")
pwd = input("Enter the password: ")

if uname in users and users[uname] == pwd:
    timestamp = datetime.now().strftime("%H:%M:%S")
    print("Access granted!")
    with open("logs.txt", "a") as wf:
        wf.write(f"Successfully logged in by {uname} at {timestamp}\n")
else:
    timestamp = datetime.now().strftime("%H:%M:%S")
    print("Access denied!")
    with open("logs.txt", "a") as wf:
        # Added \n for a new line
        wf.write(f"Failed login attempt for {uname}\n") 
        wf.write(f"Failed attempt by {uname} at {timestamp}\n")
        print("User log activity saved in logs.txt")