import numpy as np
a=np.array([1,2])
b=np.array([3,4])
c=print(np.sqrt((a*a).sum()))
print(np.linalg.norm(a))
cosangle= a.dot(b) / (np.linalg.norm(a)*np.linalg.norm(b))
print(cosangle)
angle=np.arccos (cosangle)
print(angle)
