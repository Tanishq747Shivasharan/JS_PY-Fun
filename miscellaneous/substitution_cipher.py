"""
This program implements a monoalphabetic substiution cipher.
Each character is mapped to a randomized character using a key.
Security depends on secret of the key.
"""

import string
import random
import os

chars = " " + string.punctuation + string.digits + string.ascii_letters

if not os.path.exists("key.txt"):
    key = chars.copy()
    random.shuffle(key)
    with  open("key.txt", "w") as f:
        f.write("".join(key))
else:
    with open("key.txt", "r") as f:
        key = list(f.read())


encrypt_map = dict(zip(chars, key))
decrypt_map = dict(zip(key, chars))

print("1. Encrypt")
print("2. Decrypt")
choice = input("Choose: ")

# Encrypt
if choice == "1":
    msg = input("Enter message: ")
    cipher = ""

    for letter in msg:
        if letter in encrypt_map:
            cipher += encrypt_map[letter]
        else:
            cipher += letter
# Decrypt
elif choice == "2":
    cipher = input("Enter encrypted message: ")
    org_msg = ""

    for letter in cipher:
        if letter in decrypt_map:
            org_msg += decrypt_map[letter]
        else:
            org_msg += letter

print("Result: ",cipher)