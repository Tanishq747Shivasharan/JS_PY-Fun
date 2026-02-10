# Day 10 of learning python.
# Catch ValueError when converting input to int.
val = (input("Enter a number: "))
try:
    print(int(val))
except ValueError:
    print("That's not a number(ValueError)")

# Handle file not found error.
try:
    with open("some_data.txt", r) as file:
        data = file.read()
except FileNotFoundError:
    print("File not found.")
