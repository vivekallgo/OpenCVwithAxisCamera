import cv2
cap = cv2.VideoCapture("rtsp://root:pass@192.168.1.192:554/axis-media/media.amp")

while(cap.isOpened()):
    ret, frame = cap.read()
    print(cap.get(3),"x",cap.get(4))
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()