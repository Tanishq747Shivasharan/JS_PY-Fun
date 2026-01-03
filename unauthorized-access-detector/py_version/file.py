data = "I am having fun coding in Python"

file_output = "learn.txt"

# with is a statement that takes care of the file that is opened to be closed automatically, it is a good pracitce to close all the files after the work(operations) are done on the file.
# open function returns a file object takes 2 parameters(file_path, [option])
# as is used to intentiate the file as to be a file

# 

try:
    with open(file_output, "x") as file:
        file.write(data + input("Enter something to append into the existing file: "))
        print(f"Text file '{file_output}' was created")
except FileExistsError:
    print(f"File '{file_output}' already exists")