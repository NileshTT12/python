import numpy as np
import matplotlib.pyplot as pdt
x=np.random.randn(100,2)
print(x)
pdt.scatter(x[:,0],x[:,1])
pdt.show()