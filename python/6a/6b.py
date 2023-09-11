import os
def list_files_and_subdirectories(directory):
 file_list = []
 for root, directories, files in os.walk(directory):
    for file in files:
        file_list.append(os.path.join(root, file))
 
 with open("file_list.txt", "w") as file:
    file.write("\n".join(file_list))
 
 print("List of files and subdirectories:")
 for item in file_list:
    print(item)
# Get directory path from the user
directory_path = input("Enter the directory path: ")
# Call the function
list_files_and_subdirectories(directory_path)