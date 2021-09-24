from cv2 import cv2
from cv2 import data
from djitellopy import tello
# Load the cascade
face_cascade = cv2.CascadeClassifier(data.haarcascades + 'haarcascade_frontalface_default.xml')

# To capture video from webcam.
cap = cv2.VideoCapture(0)

# To use a video file as input
# cap = cv2.VideoCapture('filename.mp4')
_, img = cap.read()
print(img.shape)
while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray,1.1,10)
    for (x, y, w, h) in faces:
        cenx = x+(w/2)
        ceny = y+(h/2)
        cv2.circle(img,(int(cenx),int(ceny)),20,(255,255,0),10)
    cv2.circle(img, (320, 240), 20, (255, 255, 0), 10)
    # Display
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xff == ord('k'):
        break
cap.release()




