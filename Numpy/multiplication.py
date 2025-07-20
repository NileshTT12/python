import numpy as np
a = np.array([1,2,3])
b = np.array([3,4,5])
dot = 0 
print("1st way from the for loop ")
for x,y in zip(a,b):
    dot+=x*y
print(dot)
#using numpy its very simple as below 
print("2nd way from the for np.sum ")
print(np.sum(a*b))
print("3rd way from the for np.dot ")
print(np.dot(a,b))
print("4th way from the for np.dot ")
print(a.dot(b))
print("5th way from the for @ ")
print(a@b)