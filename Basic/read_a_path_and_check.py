import os
path = input("Enter the path: ")
if os.path.exists(path):
    print("Path is valid")
    if os.path.isfile(path):
        print(f'This is the file buddy {path}')
    else:
        print(f'This is the folder')
else :
    print("Path is invalid")
