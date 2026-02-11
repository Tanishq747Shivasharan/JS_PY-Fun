# 🧠 PHASE 1 — Python Core for Security

## ✅ SYSTEM BUILDING + HARD CODING QUESTIONS

---

# 🟢 DAY 1 — Basic Login System

## 🛠 System Task

Build a CLI login program:

* Ask username & password
* Compare with hardcoded values

---

## 🔥 Coding Questions

1️⃣ Write a program to:

* Take username and password
* Print **Access Granted** only if both match

2️⃣ Modify program so username is **case-insensitive**

3️⃣ Print how many characters user typed in password

---

# 🟢 DAY 2 — Conditional Auth System

## 🛠 System Task

Add:

* Separate error for wrong username
* Separate error for wrong password

---

## 🔥 Coding Questions

1️⃣ Write program to check:

* Username correct but password wrong → print specific message

2️⃣ Add **elif** for admin login vs normal user

3️⃣ Implement `not` operator to block empty username/password

---

# 🟢 DAY 3 — Brute Force Simulation (3 Attempts)

## 🛠 System Task

* Allow only 3 login attempts
* Exit after failure

---

## 🔥 Coding Questions

1️⃣ Use while loop to allow max 3 attempts
2️⃣ Print remaining attempts
3️⃣ Stop program manually using `break`

---

# 🟢 DAY 4 — Function-Based Auth System

## 🛠 System Task

Create reusable authentication function:

```python
def authenticate(u, p):
```

---

## 🔥 Coding Questions

1️⃣ Return True or False instead of printing
2️⃣ Call function from main program
3️⃣ Count how many times function is called (global counter)

---

# 🟢 DAY 5 — Input Sanitization System

## 🛠 System Task

* Trim spaces
* Convert username to lowercase
* Block empty password

---

## 🔥 Coding Questions

1️⃣ Remove spaces from input
2️⃣ Block passwords shorter than 6 characters
3️⃣ Detect if password contains only numbers

---

# 🟢 DAY 6 — Multi-User Login (Lists)

## 🛠 System Task

Store usernames in list:

```python
users = ["admin", "tanishq", "root"]
```

---

## 🔥 Coding Questions

1️⃣ Check if input user exists in list
2️⃣ Print index of user if found
3️⃣ Add new user dynamically using append()

---

# 🟢 DAY 7 — Dictionary-Based Authentication

## 🛠 System Task

```python
users = {"admin":"1234", "tanishq":"pass"}
```

---

## 🔥 Coding Questions

1️⃣ Check login using dictionary
2️⃣ Print all registered users
3️⃣ Add new user via input

---

# 🟢 DAY 8 — Failed Login Logger

## 🛠 System Task

Log failed attempts to `logs.txt`

---

## 🔥 Coding Questions

1️⃣ Append failed username to file
2️⃣ Log timestamp using time module
3️⃣ Count how many lines written

---

# 🟢 DAY 9 — Log Analyzer System

## 🛠 System Task

Read logs and count failures

---

## 🔥 Coding Questions

1️⃣ Count number of failed attempts in file
2️⃣ Print unique usernames from logs
3️⃣ Detect most attacked username

---

# 🟢 DAY 10 — Safe Input System

## 🛠 System Task

Prevent crashes using try/except

---

## 🔥 Coding Questions

1️⃣ Catch ValueError when converting input to int
2️⃣ Handle file-not-found error
3️⃣ Create custom error message system

---

# 🟢 DAY 11 — Password Strength Engine

## 🛠 System Task

Classify password: Weak / Medium / Strong

---

## 🔥 Coding Questions

1️⃣ Check if password has:

* uppercase
* digit
* symbol

2️⃣ Calculate password strength score
3️⃣ Suggest improvements to weak passwords

---

# 🟢 DAY 12 — Account Lockout System

## 🛠 System Task

Lock user after 3 failures

---

## 🔥 Coding Questions

1️⃣ Store failed attempts per user in dict
2️⃣ Block user permanently after 3 fails
3️⃣ Add unlock admin command

---

# 🟢 DAY 13 — Fake Credential Database

## 🛠 System Task

Nested dict system:

```python
db = {
 "admin": {"pass":"1234", "role":"admin"}
}
```

---

## 🔥 Coding Questions

1️⃣ Print user role after login
2️⃣ Block login if role = "banned"
3️⃣ Add new fields like last_login

---

# 🟢 DAY 14 — Integrated Secure Auth System

## 🛠 System Task

Combine:

* Login
* Logs
* Lockout
* Password strength

---

## 🔥 Coding Questions

1️⃣ Modularize code into multiple functions
2️⃣ Create menu system (login/register/exit)
3️⃣ Save users to file (simulate database)

---

# 🟢 DAY 15 — Secure Login Mini Project

## 🛠 System Task

Build **full CLI Secure Login System** with:

* Multi-user
* Logs
* Lockout
* Strength checker
* File-based DB

---

## 🔥 HARD SYSTEM DESIGN QUESTIONS

1️⃣ How would you prevent brute force without lockout?
2️⃣ Why should passwords never be stored in plaintext?
3️⃣ How real systems hash passwords?

---

# 🟡 PHASE 2 — Automation & Scripting (Day 16–30)

---

# 🟡 DAY 16 — OS Module Basics

## 🛠 System Task

Build a script that prints all files in a folder.

## 🔥 Coding Challenges

1. Print current working directory
2. Count number of files in folder
3. Show only `.txt` files

---

# 🟡 DAY 17 — Run System Commands

## 🛠 System Task

Run ping or ipconfig from Python.

## 🔥 Challenges

1. Run `ping google.com`
2. Capture output to a file
3. Count ping responses

---

# 🟡 DAY 18 — Command Automation Loop

## 🛠 System Task

Run a command every 5 seconds.

## 🔥 Challenges

1. Infinite command loop
2. Stop loop with user input
3. Log execution timestamps

---

# 🟡 DAY 19 — Multi-IP Scanner Logic

## 🛠 System Task

Loop through IP list and simulate scan.

## 🔥 Challenges

1. Store IPs in list
2. Mark IP as reachable/unreachable randomly
3. Print summary report

---

# 🟡 DAY 20 — Batch URL Checker

## 🛠 System Task

Check URL format validity.

## 🔥 Challenges

1. Validate http/https prefix
2. Count invalid URLs
3. Auto-fix missing protocol

---

# 🟡 DAY 21 — Automation Error Handling

## 🛠 System Task

Prevent automation script crash.

## 🔥 Challenges

1. Handle missing file errors
2. Handle permission errors
3. Retry failed command

---

# 🟡 DAY 22 — Log Cleanup Script

## 🛠 System Task

Delete old logs.

## 🔥 Challenges

1. Delete logs older than 7 days
2. Ask confirmation before delete
3. Backup logs before deletion

---

# 🟡 DAY 23 — CLI Arguments

## 🛠 System Task

Run script with arguments.

## 🔥 Challenges

1. Accept filename from CLI
2. Accept IP from CLI
3. Show help message

---

# 🟡 DAY 24 — Script Hardening

## 🛠 System Task

Validate all user inputs.

## 🔥 Challenges

1. Block dangerous characters
2. Limit input length
3. Sanitize file paths

---

# 🟡 DAY 25 — Master Script Runner

## 🛠 System Task

Run multiple scripts from one script.

## 🔥 Challenges

1. Create menu to select script
2. Execute script dynamically
3. Log script results

---

# 🟡 DAY 26–29 — Attack vs Defense Automation

## 🔥 Challenges

1. Simulate brute-force speed test
2. Implement rate limiter
3. Optimize loop execution

---

# 🟡 DAY 30 — Automation Toolkit Mini Project

## 🛠 Build

A toolkit folder with:

* ping tool
* log cleaner
* URL checker
* IP scanner

---

# 🔵 PHASE 3 — Networking with Python (Day 31–45)

---

# 🔵 DAY 31 — IP & Ports Basics

## 🔥 Challenges

1. Print local IP
2. List common ports
3. Explain port vs service mapping

---

# 🔵 DAY 33–35 — TCP Client/Server

## 🔥 Challenges

1. Build TCP server
2. Build TCP client
3. Send secret message

---

# 🔵 DAY 36 — Port Scanner Logic

## 🔥 Challenges

1. Scan ports 20–100
2. Detect open/closed
3. Timeout handling

---

# 🔵 DAY 38 — Banner Grabbing

## 🔥 Challenges

1. Capture service banner
2. Identify service type
3. Save banners to file

---

# 🔵 DAY 45 — Network Scanner Mini Project

Build a real port scanner tool.

---

# 🟣 PHASE 4 — Web Security & OSINT (Day 46–60)

---

# 🟣 DAY 49 — requests Library

## 🔥 Challenges

1. Fetch webpage
2. Save HTML to file
3. Count words

---

# 🟣 DAY 52 — Brute-Test Logic

## 🔥 Challenges

1. Try multiple passwords on login form (simulation)
2. Implement rate limiter
3. Detect lockout response

---

# 🟣 DAY 54 — Web Scraper

## 🔥 Challenges

1. Extract page title
2. Extract all links
3. Detect admin panels

---

# 🟣 DAY 60 — Web Recon Tool

Build domain recon + email extractor tool.

---

# 🔴 PHASE 5 — Crypto & Malware Logic (Day 61–75)

---

# 🔴 DAY 62 — Hashing

## 🔥 Challenges

1. Hash password
2. Compare hashes
3. Store hash in file

---

# 🔴 DAY 67 — File Integrity Checker

## 🔥 Challenges

1. Hash file baseline
2. Detect file change
3. Alert user

---

# 🔴 DAY 71 — Signature Detection

## 🔥 Challenges

1. Blacklist hash list
2. Detect malicious file
3. Whitelist safe files

---

# 🔴 DAY 75 — Threat Detector Project

Detect suspicious files + integrity issues.

---

# ⚫ PHASE 6 — SOC & Security Tool Building (Day 76–90)

---

# ⚫ DAY 78 — Brute Force Detection

## 🔥 Challenges

1. Detect repeated failures
2. Trigger alert
3. Block IP

---

# ⚫ DAY 81 — Anomaly Detection

## 🔥 Challenges

1. Baseline login frequency
2. Detect spikes
3. Generate SOC alert

---

# ⚫ DAY 84 — CLI Security Tool

## 🔥 Challenges

1. Build security tool with arguments
2. Run scan mode
3. Run defense mode

---

# ⚫ DAY 90 — CYBER DEFENSE LAB FINAL

Combine EVERYTHING into one toolkit.