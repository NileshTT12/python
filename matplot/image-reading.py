from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
im = Image.open('/Users/nthombre/Desktop/photo-1.jpg')
arr=np.array(im)
print(arr)
print(arr.shape)
plt.imshow(arr);
plt.show()