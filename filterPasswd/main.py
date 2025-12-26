from password_checker import passwd

passwd = input("Enter your password: ")

errs =  passwd.check_passwd(passwd)
if errs == 0:
    print("Your password is strong enough")  
else:
    print("Your password is weak, please try again")
    print("Your password should contain at least 8 characters, 1 uppercase letter, 1 lowercase letter, 1 number and 1 special character")
    print("Your password should not contain any spaces")
    print("Your password should not contain any common words")
    print("Your password should not contain any common sequences")
    print("Your password should not contain any common patterns")
    print("Your password should not contain any common substrings")
    for err in errs:
        print("-",err)