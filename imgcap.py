import numpy
from cv2 import cv2
from djitellopy import tello

drone = tello.Tello()
drone.connect()
drone.streamon()

while True:
    img = drone.get_frame_read().frame
    cv2.imshow("feed", img)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break



cv2.destroyWindow()





