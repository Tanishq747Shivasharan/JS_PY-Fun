def greet(name):
    print(f"Hello {name}!") # Static way of showing the res.

if __name__ == "__main__":
    name = input("Enter your name: ")
    if not name.strip():
        print("Invalid name")
        greet("anonymous")
    else:   # This is the main function so whatever functions declared should be above the main function.
        greet(name)

# def greet(name):
#     return f"Hello {name}!" # Dynamic way of showing the result. # wrong way of defining the functions in Python.

#     Enter your name: Tanishq
# Traceback (most recent call last):
#   File "D:\Coding Languages\JS_PY-Fun\Secure_System_lab\week1_pybasics\functions.py", line 6, in <module>
#     greet(name)
#     ^^^^^
# NameError: name 'greet' is not defined

# calling a function.
print(greet("Manya"))

# function arguments.
# 1. Default arguments
# 2. Keyword arguments
# 3. Positional arguments
# 4. Arbitrary arguments

def greetWithDefault_age(name, age = 18):   # --> Default argument is age assigned with the value 18.
    print(f"Hello {name}! You are {age} years old.")

# static way of calling a function.
greetWithDefault_age("Tanishq")
greetWithDefault_age("Manya", 20) # --> No error displayed here the assigned value in the arguments given is assigned with new value that is 20.

def greetWithKeyword_arg(fname, lname): # --> keyword arguments are both fname and lname.
    print(f"Hello {fname} {lname}!")
    
# static way of calling a function.
greetWithKeyword_arg(fname = "Tanishq", lname = "Shivasharan") # --> Keyword arguments are used to assign the values to the arguments in the function.
greetWithKeyword_arg(lname = "Gundla", lname = "Manya")

def nameAge(name, age): # --> Positional arguments are name and age values are assigned to parameters based on their order in the function call.
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Suraj", 27)

print("\nCase-2:")
nameAge(27, "Suraj")