# list in python--> mutable, ordered, index-based, allows mixed datatypes, can contain duplicate items.
users = ['tanishq123', 'rahul_kumar', 'ankit99', 'priya_singh', 'chatGPT', 'alex', 'user2020']

find_user = input("Enter user to find: ")

if find_user in users:
    print(f"User {find_user} found at index {users.index(find_user)}")
else:
    print(f"User {find_user} doesn't exists!")
    if find_user not in users:
        users.append(find_user)
    print(f"User {find_user} added successfully!")

print(users)

# for find_user in users:
#     if find_user is users[find_user]:
#         print(f"Ther user {users[user]} is present in the list.")
#     else:
#         print(f"The user doesn't exist in the database!")