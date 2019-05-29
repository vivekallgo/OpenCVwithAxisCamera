import cv2
import numpy as np
cap = cv2.VideoCapture("rtsp://root:pass@192.168.1.192:554/axis-media/media.amp?resolution=640x480")

while(cap.isOpened()):
    frame = cap.read()

    # Draw a diagonal blue line with thickness of 5 px
    cv2.line(img=(np.array(frame,np.uint8)), pt1=(10, 10), pt2=(100, 10), color=(255, 0, 0), thickness=5, lineType=8, shift=0)

    cv2.imshow('frame', frame)
    
    
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()