import os
import secrets

while True:
    plain_txt = input('Enter a message: ')
    if not plain_txt:
        print("Empty message - nothing to encrypt.TRY AGAIN...")
    else:
        break
encodedPlain_txt = plain_txt.encode() # encoding the plain text to byte.

key = secrets.token_bytes(len(encodedPlain_txt)) # encoding the key to byte.

list_txt = list(encodedPlain_txt) # converting the encoded plain text to list.
list_key = list(key) # converting the key to list.

# Encryption
for i in range(len(encodedPlain_txt)):
    xor_res = list_txt[i] ^ list_key[i] # XOR operation to encrypt the plain text.
    list_txt[i] = xor_res
    
ciphertext_bytes = bytes(list_txt)
print('Encrypted message:', ciphertext_bytes.hex())

# Decryption
for i in range(len(ciphertext_bytes)):
    xor_res = list_txt[i] ^ list_key[i] # XOR operation to decrypt the plain text.
    list_txt[i] = xor_res
    
decrypted_bytes = bytes(list_txt)
print('Decrypted message:', decrypted_bytes.decode())