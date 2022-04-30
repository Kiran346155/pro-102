import cv2

cam = cv2.VideoCapture(0)

result=True

while result:
    ret, frame = cam.read()
   
    cv2.imwrite("test.jpg", frame)
    
    result=False

cam.release()

cv2.destroyAllWindows()