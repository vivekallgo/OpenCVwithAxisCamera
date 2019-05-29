import cv2
import numpy as np
cap = cv2.VideoCapture(0)#"rtsp://root:pass@192.168.1.192:554/axis-media/media.amp?resolution=640x480")

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    
     #Convert image from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get HSV value of Blue
    #  blue = np.uint8([[[255,0,0]]])
    #    hsv_blue = cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)
    #   print(hsv_blue) """

    #define blue range color in HSV
    lower_blue = np.array([110,50,50])
    high_blue = np.array([120,255,255])

    #Threshold the HSV to get only blue color
    mask = cv2.inRange(hsv,lower_blue,high_blue)

    #Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('result',res)


    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()