# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 11:32:42 2019

@author: Manish
"""

import cv2 
cv2.namedWindow('image',cv2.WINDOW_NORMAL)

img=cv2.imread(r"C:\Users\Manish\Desktop\wallpaper.jpg",0)

imS = cv2.resize(img, (600,600)) 
cv2.imshow("image",imS)
cv2.waitKey()

cv2.destroyAllWindows()
