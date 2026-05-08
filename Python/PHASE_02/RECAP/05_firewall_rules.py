# Conditionals and Booleans: Access Control Logic

user_status = 'Admin'

login_time = int(input("Enter login time: "))

if user_status == 'Admin' and 9 < login_time < 17:
    print("Access Granted")
else:
    print("Access Denied")