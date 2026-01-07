import os
import secrets

plain_txt = input('Enter a message: ')
encodedPlain_txt = plain_txt.encode() # encoding the plain text to byte.

key = secrets.token_bytes(len(plain_txt)) # encoding the key to byte.

# Encryption
for i in range(len(encodedPlain_txt)):
    encodedPlain_txt[i] ^= encodedPlain_key[i] # XOR operation to encrypt the plain text.

print('Encrypted message:', ciphertext_bytes.hex())