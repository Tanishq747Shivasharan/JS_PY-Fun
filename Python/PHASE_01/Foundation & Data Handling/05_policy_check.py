# Operators & Logic

# Operators Precedence in Python
"""
Python follows PEMDAS(Parentheses, Exponents, Multiplication, Division, Addtion, Subtraction)
1. Parentheses () - Highest precedence, operations inside parentheses are evaluated first.
2. Exponents ** - Power calculations (e.g. 2**3-->8) Evaluated from right to left.(Highest precedence)
3. Multiplication *, Division /, Floor Division //, Modulus % - Evaluated from left to right.(Lower precedence)
4. Addition +, Subtraction - - Evaulated from left to right.
"""

password = input("Enter a password: ")
is_encrypted = True

len_passwd = len(password)

if len_passwd >= 12 and is_encrypted == True:
    print("Password Set")
else:
    print("Please make sure the lenght of the password is greater than 12 and it is encrypted!")