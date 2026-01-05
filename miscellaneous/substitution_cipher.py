"""
This program implements a monoalphabetic substiution cipher.
Each character is mapped to a randomized character using a key.
Security depends on secret of the key.
"""

import string
import random

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key: {key}")

# Encryption
msg = input("Enter a message to encrypt: ")
cipher = ""

for letter in msg:
    idx = chars.index(letter)
    cipher += key[idx]

print(f"Original message: {msg}")
print(f"Encrypted message: {cipher}")

# Decryption
cipher = input("Enter a message to decrypt: ")
org_msg = ""

for letter in cipher:
    idx = key.index(letter)
    org_msg += chars[idx]

print(f"Encrypted message: {cipher}")
print(f"Decrypted message: {org_msg}")