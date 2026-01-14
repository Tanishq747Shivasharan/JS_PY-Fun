def greet(name):
    print(f"Hello {name}!") # Static way of showing the res.

if __name__ == "__main__":
    name = input("Enter your name: ")   # This is the main function so whatever functions declared should be above the main function.
    greet(name)

# def greet(name):
#     return f"Hello {name}!" # Dynamic way of showing the result. # wrong way of defining the functions in Python.

#     Enter your name: Tanishq
# Traceback (most recent call last):
#   File "D:\Coding Languages\JS_PY-Fun\Secure_System_lab\week1_pybasics\functions.py", line 6, in <module>
#     greet(name)
#     ^^^^^
# NameError: name 'greet' is not defined