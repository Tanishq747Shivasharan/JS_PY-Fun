# 1. Import the modules (json, datetime, pathlib)
import json
import os
import datetime
from pathlib import Path

# 2. Create a folder named "logs" (use Path.mkdir with exist_ok=True)
dire = Path("py_version/logs")
dire.mkdir(exist_ok=True) # exist_ok=True prevents erros if the folder already exists

# 3. Define your log file path inside that folder, e.g., logs/system_log.json
log_file = dire/"system_log.json"

# 4. If the file does NOT exist yet:
#      - Create it and dump an empty list [] to start the JSON structure
if not log_file.exists():
    with open(log_file, "w") as f:
        json.dump([], f)

# 5. If it DOES exist:
#      - Load the existing list of logs (using json.load)
with open(log_file, "r") as f:
    Logs = json.load(f)

# 6. When adding a new log:
#      - Create a dictionary like:
#        {
#          "timestamp": current time,
#          "event": "something happened",
#          "severity": "INFO"
#        }
#      - Append it to the list
#      - Write the list back into the same file (using json.dump)
current_t = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")

event = input("Enter event to log: ")
severity = input("Enter severity of event: ")

log_entry = {
    "timestamp": current_t,
    "event": event,
    "severity": severity
}

Logs.append(log_entry)
with open(log_file, "w") as f:
    json.dump(Logs, f, indent=4)

# 7. Print the new log entry to the console for visibility
print(log_entry)


