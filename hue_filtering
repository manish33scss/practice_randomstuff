import cv2 
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.namedWindow('image2',cv2.WINDOW_NORMAL)
cv2.namedWindow('image3',cv2.WINDOW_NORMAL)

img=cv2.imread(r"C:\Users\Manish\Desktop\wallpaper.jpg")
hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
imS = cv2.resize(hsv_img, (600,600)) #resize the window 
#cv2.imshow("image",imS)
cv2.imshow("image",imS[:,:,0])
cv2.imshow("image2",imS[:,:,1])
cv2.imshow("image3",imS[:,:,2])

cv2.waitKey()

cv2.destroyAllWindows()
