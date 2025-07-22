import os 
req_file=input("Enter the file name please :")
path="/Users/nthombre/"
#print(list(os.walk(path)))
for a,b,c in os.walk(path):
   #print(c)
   for each in c:
     if each == req_file:
        print(os.path.join(a,each))