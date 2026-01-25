real_uname = "WisdomHaki"
real_password = "Robin@321&#"

global_fun_counter = 0

def reusable_code(name, password):
    global global_fun_counter
    global_fun_counter += 1
    if name == real_uname and password == real_password:
        print(f"Welcome {name}! Login successful")
        return True
    else:
        print(f"Login failed for {name}")
        return False

if  __name__ == "__main__":
    # Test users
    reusable_code(real_uname, real_password)
    reusable_code("Tanishq", "1234")
    print(f"The Function has been called for {global_fun_counter} times.")














































# learning Phase...
# def greet(name):
#     print(f"Hello {name}!") # Static way of showing the res.

# if __name__ == "__main__":
#     name = input("Enter your name: ")
#     if not name.strip():
#         print("Invalid name")
#         greet("anonymous")
#     else:   # This is the main function so whatever functions declared should be above the main function.
#         greet(name)

# # def greet(name):
# #     return f"Hello {name}!" # Dynamic way of showing the result. # wrong way of defining the functions in Python.

# #     Enter your name: Tanishq
# # Traceback (most recent call last):
# #   File "D:\Coding Languages\JS_PY-Fun\Secure_System_lab\week1_pybasics\functions.py", line 6, in <module>
# #     greet(name)
# #     ^^^^^
# # NameError: name 'greet' is not defined

# # calling a function.
# print(greet("Manya"))

# # function arguments.
# # 1. Default arguments
# # 2. Keyword arguments
# # 3. Positional arguments
# # 4. Arbitrary arguments

# def greetWithDefault_age(name, age = 18):   # --> Default argument is age assigned with the value 18.
#     print(f"Hello {name}! You are {age} years old.")

# # static way of calling a function.
# greetWithDefault_age("Tanishq")
# greetWithDefault_age("Manya", 20) # --> No error displayed here the assigned value in the arguments given is assigned with new value that is 20.

# def greetWithKeyword_arg(fname, lname): # --> keyword arguments are both fname and lname.
#     print(f"Hello {fname} {lname}!")
    
# # static way of calling a function.
# greetWithKeyword_arg(fname = "Tanishq", lname = "Shivasharan") # --> Keyword arguments are used to assign the values to the arguments in the function.
# greetWithKeyword_arg(lname = "Gundla", fname = "Manya")

# def nameAge(name, age): # --> Positional arguments are name and age values are assigned to parameters based on their order in the function call.
#     print("Hi, I am", name)
#     print("My age is ", age)

# print("Case-1:")
# nameAge("Suraj", 27)

# print("\nCase-2:")
# nameAge(27, "Suraj")

# def power_cal(*numbers):    # *numbers is an tuple --> *args --> tuple
#     total = 0    
#     for n in numbers:
#         if (n % 2==0):
#             res = n**2
#         else:
#             res = n**3
#         total = total + res
#     return total

# print("Power Score: ", power_cal(2,3,6,7,9,0,1))    # --> It's like saying that we are passing multiple arguments to the function. Sometimes, we don't know how many values user will pass to a function. So Py says: Fine, I'll catch them all in one variable.

# def print_marks(**kwargs):    # **marks is an dictionary --> **kwargs --> dictionary
#     total = 0
#     avg = 0
#     for Subject, marks in kwargs.items():
#         print(f"{Subject} : {marks}")
#         total = total + marks
#     avg = total/3
#     print(f"Total = {total}")
#     print(f"Average = {avg}")

# print_marks(Maths=85, Physics=90, Chemistry=88)

# # Function within Function(Inner function.)
# def f1():
#     s = 'I love Python programming language.'
#     def f2():
#         print(s)
    
#     f2()
# f1()

# # Anonymous Function(lambda keyword is used to create an anonymous functions.)
# check = lambda x : x if x%2==0 else x
# print(check(10))  
# print(check(7))  
# # Extracting numbers greater than 50 from this given list.
# marks = [45, 78, 62, 30, 90, 55]
# extract = list(filter(lambda x : x > 50, marks))
# print(extract)

# # Recursive Function 
# def factorial(n):
#     if n == 0:  
#         return 1
#     else:
#         return n * factorial(n - 1) 
      
# print(factorial(4))