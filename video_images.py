# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 15:16:06 2019

@author: student
"""

import cv2
vidcap = cv2.VideoCapture(r'D:\Manish_Mtech\samplevideos\c_r.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print ('Read a new frame: ', success)
  count += 1