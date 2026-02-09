
def encrypt(plain_text, rails):
    """
    Encrypts text using Rail Fence cipher
    """
    if rails == 1:
        return plain_text
    
    # Create rails
    rails_list = [""] * rails
    
    # Track current rail and direction
    current_rail = 0
    direction_down = True
    
    # Place each character on appropriate rail
    for char in plain_text:
        rails_list[current_rail] += char
        
        # Change direction at top and bottom rails
        if current_rail == 0:
            direction_down = True
        elif current_rail == rails - 1:
            direction_down = False
        
        # Move to next rail
        if direction_down:
            current_rail += 1
        else:
            current_rail -= 1
    
    # Join all rails to create cipher text
    return ''.join(rails_list)

def decrypt(cipher_text, rails):
    """
    Decrypts text using Rail Fence cipher
    """
    if rails == 1:
        return cipher_text
    
    # Create a matrix to mark positions
    rail_matrix = [['' for _ in range(len(cipher_text))] for _ in range(rails)]
    
    # Mark the positions where characters should be placed
    current_rail = 0
    direction_down = True
    
    for i in range(len(cipher_text)):
        rail_matrix[current_rail][i] = '*'
        
        if current_rail == 0:
            direction_down = True
        elif current_rail == rails - 1:
            direction_down = False
        
        if direction_down:
            current_rail += 1
        else:
            current_rail -= 1
    
    # Fill the matrix with cipher text characters
    index = 0
    for rail in range(rails):
        for col in range(len(cipher_text)):
            if rail_matrix[rail][col] == '*':
                rail_matrix[rail][col] = cipher_text[index]
                index += 1
    
    # Read the matrix in zigzag pattern to get original text
    result = []
    current_rail = 0
    direction_down = True
    
    for i in range(len(cipher_text)):
        result.append(rail_matrix[current_rail][i])
        
        if current_rail == 0:
            direction_down = True
        elif current_rail == rails - 1:
            direction_down = False
        
        if direction_down:
            current_rail += 1
        else:
            current_rail -= 1
    
    return ''.join(result)

def main():
    """
    Main program loop for Rail Fence cipher
    """
    print("=== Rail Fence Cipher ===")
    
    while True:
        print("\n1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        try:
            choice = int(input("\nEnter your choice (1-3): "))
            
            if choice == 1:
                plain_text = input("Enter the message to encrypt: ")
                rails = int(input("Enter the number of rails (minimum 2): "))
                
                if rails < 1:
                    print("Error: Number of rails must be at least 1")
                    continue
                
                cipher_text = encrypt(plain_text, rails)
                print(f"Encrypted message: {cipher_text}")
                
            elif choice == 2:
                cipher_text = input("Enter the message to decrypt: ")
                rails = int(input("Enter the number of rails (minimum 2): "))
                
                if rails < 1:
                    print("Error: Number of rails must be at least 1")
                    continue
                
                plain_text = decrypt(cipher_text, rails)
                print(f"Decrypted message: {plain_text}")
                
            elif choice == 3:
                print("Goodbye!")
                break
                
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
                
        except ValueError:
            print("Error: Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
    
