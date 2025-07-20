
import os 
req_file_name=input("enter the file name which you want to search ? :")
path="/Users/nthombre/Study/python/test"
for a,b,c in os.walk(path):
    #print(os.path.join(a,c))
    print(a)