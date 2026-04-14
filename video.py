import cv2
vedio = cv2.VideoCapture('navratri reel.mp4')
while True:
    ret,frame = vedio.read()
    if ret == False:
        break
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(grey,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('img',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vedio.release()
cv2.destroyAllWindows()
