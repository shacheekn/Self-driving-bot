from sensor import Motor
from lanedetection import getLaneCurve
import cam as webcam
import cv2

##################################################
motor = Motor(25,27,22,26,5,6)
cap = cv2.VideoCapture(0)
##################################################



if _name_ == '_main_':

    while True:
        success ,img = cap.read() # GET THE IMAGE
        img = cv2.resize(img,(640,480)) # RESIZE
        cv2.imshow('image',img)

        curveVal= getLaneCurve(img,1)

        sen = 1.3  # SENSITIVITY
        maxVAl= 0.3 # MAX SPEED
        if curveVal>maxVAl:curveVal = maxVAl
        if curveVal<-maxVAl: curveVal =-maxVAl
    #print(curveVal)
        if curveVal>0:
            sen =1.7
            if curveVal<0.05: curveVal=0
        else:
            if curveVal>-0.08: curveVal=0
        motor.move(0.20,curveVal*sen,0.05)
        cv2.waitKey(1)