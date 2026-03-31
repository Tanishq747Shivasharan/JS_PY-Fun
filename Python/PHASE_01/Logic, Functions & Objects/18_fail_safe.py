# Exception Handling

try:
    a = 10/0
except ZeroDivisionError:
    print("Cannnot divide by zero!")

try:
    with open ("file.txt", "r") as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print("File doesn't exist!")