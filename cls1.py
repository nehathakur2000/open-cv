import cv2
face_cascade=cv2.CascadeClassifier("facefile.xml")
vid = cv2.VideoCapture(0)

while True:
    ret,frame = vid.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
        cv2.imshow("camera",frame)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
vid.release()
cv2.distroyAllWindows()




