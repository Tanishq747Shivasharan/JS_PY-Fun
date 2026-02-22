import os

current_dir = os.getcwd()
print(current_dir)  # Prints the current Path of working directory.

change_dir = os.chdir("TEST_DIR")
print("Changed directory into TEST_DIR") # Similar to cd command in Linux OS

ls = os.listdir()
print("The files in current directory are: ", ls) # Similar to the ls command in Linux OS

try:
    os.mkdir("TEST_DIR2") # Make(Create) Directory similar to mkdir command in Linux OS
    print(f"Successfully created the {mkdir} folder.")
except FileExistsError:
    print("The folder already exists")
except Exception as e:
    print("Error: ",e)

os.remove("sample.txt") # not recommanded to execute as it will cause loss of all files contained in the current working directory.

# The professional way to handle things is using.
if os.path.exists("sample.txt"):
    os.remove("sample.txt")
else:
    print("The file does not exist")

# rename file using
os.rename("sample.txt","demo.txt")