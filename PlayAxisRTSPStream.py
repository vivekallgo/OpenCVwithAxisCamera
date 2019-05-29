import cv2
cap = cv2.VideoCapture("rtsp://root:pass@192.168.1.192:554/axis-media/media.amp?resolution=640x480")

# For Webcam
#cap = cv2.VideoCapture(0)
# Note: Only works with webcam--------------------------
#set height
#print(ret)
#set width
#ret= cap.set(4,240)
#print(ret)

#--------------------------------------------------------



while(cap.isOpened()):
    ret, frame = cap.read()

    # Print resolution of the camera
    #print(cap.get(3),"x",cap.get(4))

    

    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()