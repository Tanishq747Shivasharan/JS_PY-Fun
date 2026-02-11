""" 
1. Ask the user to enter a message.
2. Ask the user for a shift number.
3. For each letter in the message:
     - Shift it by the given number.
     - Wrap around if it goes past 'Z' or 'z'.
4. Print the encrypted message. """

u_msg = input("Enter your message: ") 
u_num = int(input("Enter a shift number: "))

# ord('A') converts the character 'A' to its ASCII value that is 65.
# chr(68) converts the ASCII value 68 to its character that is 'D'.

for ch in u_msg:
    if ch.isalpha():
        if ch.isupper():
            print(chr(((ord(ch) - ord('A') + u_num) % 26) + ord('A')), end='')
        else:
            print(chr(((ord(ch) - ord('a') + u_num) % 26) + ord('a')), end='')
    else:        
        print(ch, end='')
