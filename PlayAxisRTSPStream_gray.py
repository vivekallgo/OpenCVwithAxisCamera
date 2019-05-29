import cv2
cap = cv2.VideoCapture("rtsp://root:pass@192.168.1.192:554/axis-media/media.amp?resolution=640x480")

while(cap.isOpened()):
    ret, frame = cap.read()
    
    #Convert image from BGR to Gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('Vivek', gray)
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()