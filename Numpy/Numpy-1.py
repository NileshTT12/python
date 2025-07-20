import numpy as np
L = [1,2,3,4]
A = np.array([5,6,7,8])
print(f'List is {L}')
print(f'Array is {A}')
print(f' when you multiple the List by 2 {L*2}')
print(f' when you multiple the Array by 2 {A*2}')
#if you want to add manually +3 to the list use below for loop 
L2=[]
for e in L:
    L2.append(e+3)
    print(L2)
