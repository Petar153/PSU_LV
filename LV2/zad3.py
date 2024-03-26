import numpy as np
import matplotlib.pyplot as plt
import scipy

img = plt.imread("tiger.png")
img = img[:,:,0].copy()
print(img.shape)
print(img.dtype)
#img2=scipy.ndimage.rotate(img, 270) #rotiranje
img2=img[:,::-1,:]
plt.figure()
plt.imshow(img2, cmap="gray")
plt.show()
