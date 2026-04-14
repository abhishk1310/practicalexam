import cv2 
img = cv2.imread('dadaji.jpg')
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')  
mouths = mouth_cascade.detectMultiScale(grey,1.3,5)
for (x,y,w,h) in mouths:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)      
cv2.imshow('img',img)
cv2.waitKey(0)      
cv2.destroyAllWindows()
    