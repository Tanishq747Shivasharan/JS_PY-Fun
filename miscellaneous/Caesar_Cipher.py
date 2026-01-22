""" 
Caesar Cipher Implementation
1. Ask the user to enter a message.
2. Ask the user for a shift number.
3. For each letter in the message:
     - Shift it by the given number.
     - Wrap around if it goes past 'Z' or 'z'.
4. Print the encrypted message.
5. Decrypt the message back to original.
"""

def caesar_encrypt(message, shift):
    """Encrypt a message using Caesar cipher with given shift."""
    if not message:
        return ""
    
    encrypted = ''
    shift = shift % 26 
    
    for ch in message:
        if ch.isalpha():
            if ch.isupper():
                ascii_val = ord(ch) - ord('A')
                shifted = (ascii_val + shift) % 26
                encrypted += chr(shifted + ord('A'))
            else:
                ascii_val = ord(ch) - ord('a')
                shifted = (ascii_val + shift) % 26
                encrypted += chr(shifted + ord('a'))
        else:
            encrypted += ch
    return encrypted

def caesar_decrypt(message, shift):
    """Decrypt a message using Caesar cipher with given shift."""
    if not message:
        return ""
    
    decrypted = ''
    shift = shift % 26  
    
    for ch in message:
        if ch.isalpha():
            if ch.isupper():
                # Handle uppercase letters
                ascii_val = ord(ch) - ord('A')
                shifted = (ascii_val - shift) % 26
                decrypted += chr(shifted + ord('A'))
            else:
                # Handle lowercase letters
                ascii_val = ord(ch) - ord('a')
                shifted = (ascii_val - shift) % 26
                decrypted += chr(shifted + ord('a'))
        else:
            decrypted += ch
    return decrypted

def get_valid_input():
    """Get valid message and shift number from user."""
    while True:
        try:
            message = input("Enter your message: ").strip()
            if not message:
                print("Error: Please enter a non-empty message.")
                continue
            
            shift_input = input("Enter a shift number: ").strip()
            shift = int(shift_input)
            
            return message, shift
            
        except ValueError:
            print("Error: Please enter a valid integer for the shift number.")
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")
            return None, None

# Main program
def main():
    """Main program function."""
    print("Caesar Cipher Program!")
    
    message, shift = get_valid_input()
    
    if message is None:
        return
    
    print(f"\nOriginal message: {message}")
    print(f"Shift number: {shift}")
    
    # Encryption
    encrypted_message = caesar_encrypt(message, shift)
    print(f"Encrypted message: {encrypted_message}")
    
    decrypted_message = caesar_decrypt(encrypted_message, shift)
    print(f"Decrypted message: {decrypted_message}")
    
    if message == decrypted_message:
        print("Encryption/Decryption successful!")
    else:
        print("Error: Decryption doesn't match original message!")

if __name__ == "__main__":
    main()