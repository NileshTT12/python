import os 
path=input("Enter the path :")
new=os.listdir(path)
print(new)
p1=new[0]
p2= os.path.join(path,new[1])
print(p2)
if os.path.isfile(p2):
    print (f' THis is the the File {p2}')
else:
    print (f' This is the Director {p2}')
