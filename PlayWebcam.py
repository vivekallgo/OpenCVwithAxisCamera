import cv2
cap = cv2.VideoCapture(0)#"rtsp://root:pass@192.168.1.192:554/axis-media/media.amp?resolution=640x480")

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()