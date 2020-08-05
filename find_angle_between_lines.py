# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 01:15:47 2020

@author: manish kumar

Angle between 2 lines :
    m1, m2 (gradient/slope)
    tan O = (mod(m1-m2)/(1+m1m2)) ; m1,m2 != -1


"""


import cv2
import math

cap = cv2.imread(r"D:\Work\Data_files\data\angles.jpg")
pointsList = []


def gradient(pt1,pt2):
    return (pt2[1] - pt1[1]) / (pt2[0]- pt1[0])


def getAngle(pointsList):
    pt1 , pt2, pt3 = pointsList[-3:]
    m1 = gradient(pt1,pt2)
    m2 = gradient(pt1, pt3)
    angle = math.atan((m2-m1)/(1+(m1*m2)))
    inDegree = round (math.degrees(angle))
    cv2.putText(cap, str(inDegree) , (pt1[0]-40 , pt1[1]-20), cv2.FONT_HERSHEY_TRIPLEX ,1, (255,0,255) , 1)
    #print(inDegree)


def mouseEvent(event, x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        size = len(pointsList)
        if size !=  0 and (size % 3) != 0:
            cv2.line (cap , tuple(pointsList[round((size-1)/3)*3]), (x,y) , (0,255,255), 1)
        cv2.circle(cap, (x,y) , 5,(255,0,0 ) , cv2.FILLED)
        pointsList.append([x,y])



while True:
    if len(pointsList) % 3 == 0 and len(pointsList) !=0:
        getAngle(pointsList)


    cv2.imshow("Image" , cap)
    cv2.setMouseCallback("Image", mouseEvent)
    if cv2.waitKey(1 ) & 0xFF == ord ('q'):
        pointsList = []
        cap = cv2.imread(r"D:\Work\Data_files\data\angles.jpg")
cap.release()
cv2.destroyAllWindows()
