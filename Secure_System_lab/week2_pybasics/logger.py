from datetime import datetime
import json
import os

users = {
    "admin": "1234",
    "tanishq": "pass"
}

# files to store locked users and failed attempts
lock_file = "locked_users.json"
log_file = "logs.txt"

# load locked users and failed attempts from file
def load_lock_data():
    if os.path.exists(lock_file):
        with open(lock_file, "r") as f:
            return json.load(f)
    return {"failed_attempts": {}, "locked_users": []}

# save lock data to file
def save_lock_data(data):
    with open(lock_file, "w") as f:
        json.dump(data, f)

# Load existing lock data
lock_data = load_lock_data()
failed_attempts = lock_data["failed_attempts"]
locked_users = lock_data["locked_users"]

uname = input("Enter the username: ")
pwd = input("Enter the password: ")
failed_attempt = 0

timestamp = datetime.now().strftime("%H:%M:%S")

# Check if user is already locked
if uname in locked_users:
    print("This account has been locked due to too many failed attempts.")
    with open(log_file, "a") as wf:
        wf.write(f"BLOCKED_ATTEMPT | user={uname} | time={timestamp}\n")
else:
    # Check credentials
    if uname in users and users[uname] == pwd:
        print("Access granted!")
        # Reset failed attempts on successful login
        if uname in failed_attempts:
            del failed_attempts[uname]
        with open(log_file, "a") as wf:
            wf.write(f"SUCCESS | user={uname} | time={timestamp}\n")
    else:
        # Increment failed attempts
        if uname not in failed_attempts:
            failed_attempts[uname] = 1
        else:
            failed_attempts[uname] += 1
        
        current_failures = failed_attempts[uname]
        print(f"Attempt {current_failures} failed.")
        
        # Check if user should be locked
        if current_failures >= 3:
            if uname not in locked_users:
                locked_users.append(uname)
            print("Too many failed attempts. Your account has been locked.")
            with open(log_file, "a") as wf:
                wf.write(f"LOCKED | user={uname} | time={timestamp}\n")
        else:
            print("Access denied!")
            with open(log_file, "a") as wf:
                wf.write(f"FAILED | user={uname} | time={timestamp}\n")

# Save updated lock data
save_lock_data({"failed_attempts": failed_attempts, "locked_users": locked_users})

# Count total log entries
line_counter = 0
if os.path.exists(log_file):
    with open(log_file, "r") as crf:
        for _ in crf:
            line_counter += 1

print("Total number of activities:", line_counter)
print("User log activity saved in logs.txt")

# Admin unlock command
if uname == "admin" and users.get("admin") == pwd:
    print("\n--- ADMIN COMMANDS ---")
    print("Locked users:", locked_users)
    if locked_users:
        unlock_cmd = input("Type 'unlock all' to unlock all users, or enter username to unlock: ")
        
        if unlock_cmd == "unlock all":
            locked_users.clear()
            # Also clear failed attempts for all users
            for user in list(failed_attempts.keys()):
                if user in users:  # Only clear for valid users
                    del failed_attempts[user]
            print("All users have been unlocked!")
            with open(log_file, "a") as wf:
                wf.write(f"ADMIN_UNLOCK_ALL | admin={uname} | time={timestamp}\n")
        elif unlock_cmd in locked_users:
            locked_users.remove(unlock_cmd)
            if unlock_cmd in failed_attempts:
                del failed_attempts[unlock_cmd]
            print(f"User '{unlock_cmd}' has been unlocked!")
            with open(log_file, "a") as wf:
                wf.write(f"ADMIN_UNLOCK | admin={uname} | target={unlock_cmd} | time={timestamp}\n")
        else:
            print("Invalid username or user not locked.")
    
    # Save any changes from admin actions
    save_lock_data({"failed_attempts": failed_attempts, "locked_users": locked_users})
