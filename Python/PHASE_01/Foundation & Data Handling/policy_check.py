# Operators & Logic

password = input("Enter a password: ")
is_encrypted = True

len_passwd = len(password)

if len_passwd >= 12 and is_encrypted == True:
    print("Password Set")
else:
    print("Please make sure the lenght of the password is greater than 12 and it is encrypted!")