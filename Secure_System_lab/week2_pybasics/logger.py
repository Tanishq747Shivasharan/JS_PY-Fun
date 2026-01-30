# Dictionary based authentication.
users = {
    "admin" : "1234",
    "tanishq": "pass"
}

uname = input("Enter the username: ")
pwd = input("Enter the password: ")

if uname in users and users[uname] == pwd:
    print("Access granted!")
else:
    print("Access denied!")
    with open("logs.txt", "a") as wf:
        # Added \n for a new line
        wf.write(f"Failed login attempt for {uname}\n") 
        print("User log activity saved in logs.txt")
