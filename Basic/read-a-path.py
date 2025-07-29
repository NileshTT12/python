import os 
path = input("Please enter the path :")
df=os.listdir(path)
p1=df[1]
p2=os.path.join(path,df[5])
print(p2)
if os.path.isfile(p2):
    print("this is the file ")
else:
    print("not a file")