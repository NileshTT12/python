import os 
import sys
path1 = input("Enter the path :")
if os.path.exists(path1):
    df1=os.listdir(path1)
    print(df1)
else:
    print("Please enter the valid path")
    sys.exit()
j1=os.listdir(path1)
for each in j1:
    new=os.path.join(path1,each)
    if os.path.isfile(new):
        print (f" this is the file {new}")
    else:
        print(f"this is not the file {new}")
    