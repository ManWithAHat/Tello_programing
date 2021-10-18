import numpy
from cv2 import cv2
from cv2 import data
from djitellopy import tello

import functions
from functions import *


drone = functions.inittello()
drone.takeoff()

face_cascade = cv2.CascadeClassifier(data.haarcascades + 'haarcascade_frontalface_default.xml')

PID = [0.5, 0.5, 0]

while True:
    img = telloframe(drone)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    dif = [0, 0, 0]
    wxis = 0
    for (x, y, w, h) in faces:
        if w > wxis:
            wxis = w
        cenx = x + (w / 2)
        ceny = y + (h / 2)
        cv2.circle(img, (int(cenx), int(ceny)), 5, (255, 255, 0), 5)
        dif = [cenx - 320, ceny - 240, 175 - w]
    cv2.circle(img, (180, 120), 5, (255, 255, 0), 5)
    print(dif)
    functions.adjust(drone,dif)
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xff == ord('k'):
        break

cv2.destroyAllWindows()
drone.land()

