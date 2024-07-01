#main.py runs the translator 
import cv2

test = cv2.VideoCapture(0)

while True:
   success,img=test.read()
   cv2.imshow("test",img)
   cv2.waitKey(1)
   cv2.imwrite("resources/test.png",img)
   i+=1