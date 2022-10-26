import cv2
import numpy as np
from matplotlib import pyplot as plt


resim = cv2.imread("resim.png",0)
cv2.imshow("manzara",resim)
cv2.waitKey()


hist=np.zeros(256) # hist dizisinin tüm elemanlarını sıfır yapar
[w,h]=resim.shape
for i in range(h):
    for j in range(w):
         renk = resim[j,i] # renk değişkeni resim matrisindeki ilgili pixelin değerini verir.
         hist[renk]=hist[renk]+1   # pixel dğerlerinin kaç tane olduğunu bulur.

a= 0   # a değişkeni  sıra ile pixel değerini artırmak için tanımladıö
for k in range(256):
    print(a,".pixel",hist[k])  # a pixel değerini , hist[renk] ise o pixel değerinden kaç tane olduğunu gösterir
    a=a+1


plt.plot(hist)
plt.show()
cv2.waitKey()



