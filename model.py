import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#input videeo from files
cap = cv2.VideoCapture('facerecognition.mp4')

while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # read image and convert to grayscale
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # detect faces

   
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    cv2.imshow('img', img)
    #draw rectangles outside of images and show 

    k = cv2.waitKey(30) & 0xff
    if k==27:
        print(len(faces))
        break
    #esc stops
# Release the videocapture 
cap.release()
