users = ['tanishq123', 'rahul_kumar', 'ankit99', 'priya_singh', 'chatGPT', 'alex', 'user2020']

# while True:
#     print("----------------------------------------------------------")
#     print("\nEnter `quit` for exiting the program")
#     print("Enter `add` for adding new uesr to list")
#     print("Enter `ls` for viewing the full list of usernames")
#     print("Enter `find` for searching a specific user from the list")
#     print("----------------------------------------------------------")
    
#     user_cmd = input("Enter your choice: ")

#     if user_cmd == 'add':
#         new_user = input("Enter the new username: ")
#         users.append(new_user)
#         print(f"User {new_user} added successfully!")
#         print(users)
#     elif user_cmd == 'ls':
#         for i in users:
#             print(i)
#     elif user_cmd == 'find':
#         find_user = input("Enter the username you want to search: ")
#         if find_user in users:
#             print(f"User {find_user} found at index {users.index(find_user)}")
#         else:
#             print(f"User {find_user} doesn't exists!")
#     elif user_cmd == 'quit':
#         print("Process terminated!")
#         break
#     else:
#         print("Invalid input! Please try again.")