import os

def show_current_directory():
    print("Current Directory:", os.getcwd())

def list_files():
    print("\nFiles and Folders:")
    for item in os.listdir():
        print("-", item)

def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        print("Folder created successfully.")
    except FileExistError:
        print("Folder already exists.")
    except Exception as e:
        print("Error:",e)


def delete_files(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print("File deleted.")
    else:
        print("File not found.")

def rename_file(old_name, new_name):
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print("File renamed.")
    else:
        print("File not found.")

def main():
    while True:
        print("\n--- Secure Directory Inspector ---")
        print("1. Show Current Directory")
        print("2. List Files")
        print("3. Create folder")
        print("4. Delete File")
        print("5. Rename file")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_current_directory()
        elif choice == "2":
            list_files()
        elif choice == "3":
            folder = input("Enter folder name: ")
            create_folder(folder)
        elif choice == "4":
            file = input("Enter file name to delete: ")
            delete_file(file)
        elif choice == "5":
            old = input("Old file name: ")
            new = input("New file name: ")
            rename_file(old, new)
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()