import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread(r"C:\Users\Manish\Desktop\wallpaper.jpg")
hist=cv2.calcHist([img], [0], None, [256], [0,256]) # (img,channel,mask,histsize,range)
plt.hist(img.ravel(), 256, [0,256])
plt.show()
color=('b', 'g', 'r')
#to separate color in eeach hist
for i, col in enumerate (color):
    hist2=cv2.calcHist([img], [i], None, [256], [0,256]) # (img,channel,mask,histsize,range)
    plt.plot(hist2,color=col)
    plt.xlim([0,256])

plt.show()
