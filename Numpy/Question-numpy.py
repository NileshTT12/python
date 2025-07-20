import numpy as np
a = np.array([[1,1],[1.5,4]])
b = np.array([2200,5050])
c=np.linalg.solve(a,b)
print(c)
x=np.array([[1,2],[2,3]])
print(np.linalg.inv(x))