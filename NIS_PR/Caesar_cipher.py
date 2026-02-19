# Caesar Cipher Program
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():   # Check if letter
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char   # Keep spaces/symbols same
    return result

def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result

# ---- Main Program ----
text = input("Enter Text: ")
shift = int(input("Enter Shift Key: "))

encrypted = encrypt(text, shift)
print("Encrypted Text:", encrypted)

decrypted = decrypt(encrypted, shift)
print("Decrypted Text:", decrypted)
