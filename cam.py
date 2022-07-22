import cv2
if _name_ == '_main_':
    cap = cv2.VideoCapture(0)
    while True:
        _, img = cap.read() # GET THE IMAGE
        img = cv2.resize(img,(640,480)) # RESIZE
        cv2.imshow('imgage',img)
        cv2.waitKey(1)