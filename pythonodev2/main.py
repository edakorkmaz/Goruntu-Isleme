import cv2
import numpy as np

resim = cv2.imread("resim.png",0)
cv2.imshow("manzara",resim)
cv2.waitKey()

deger= np.max(resim)

[a,b]=resim.shape
YeniResim = np.zeros([a,b], dtype=np.uint8)
for i in range(a):
    for j in range(b):
        YeniResim[i,j] = deger - resim[i,j]

cv2.imshow("manzara",YeniResim )
cv2.waitKey()
