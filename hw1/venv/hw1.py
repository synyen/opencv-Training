import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

img_bgr = cv2.imread('Bird feeding 3 low contrast.tif')

img_rgb = img_bgr[:, :, ::-1]

plt.imshow(img_rgb)
plt.show()

plt.hist(img_rgb.ravel(), 256, [0, 256])
plt.title('Original')
plt.savefig('Original Histogram', dpi=300)
plt.show()

img_new = (np.arctan((img_rgb - 128.0)/32.0))
plt.imshow(img_new)
plt.savefig('New image')
plt.show()


plt.hist(img_new.ravel(), 256, [0, 256])
plt.title('Output')
plt.savefig('Output Histogram')
plt.show()

x = np.arange(0, 255, 0.1)
y = np.arctan((x-128.0)/32.0)

plt.plot(x, y)
plt.title("Figure of S = T(r)")
plt.xlabel("r")
plt.ylabel("S")
plt.savefig('Figure of s = T(r)', dpi=300)
plt.show()



