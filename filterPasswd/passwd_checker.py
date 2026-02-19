import re
import getpass

print("Enter Password:")
password = getpass.getpass()   # Hides password while typing

# Check length
if len(password) <= 8:
    print("Password must be more than 8 characters.")
    exit()

# Check for at least one letter
if not re.search(r"[A-Za-z]", password):
    print("Password must contain at least one letter.")
    exit()

# Check for at least one digit
if not re.search(r"[0-9]", password):
    print("Password must contain at least one digit.")
    exit()

# Check for at least one special character (#, %, &, @)
if not re.search(r"[#%@&]", password):
    print("Password must contain at least one special character (#, %, &, @).")
    exit()

print("Strong Password! Authentication Successful.")