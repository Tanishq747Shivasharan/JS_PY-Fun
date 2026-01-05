import string
import random

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)

key = chars.copy()

# print(chars)

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

