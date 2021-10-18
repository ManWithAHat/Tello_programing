import cv2.cv2
from djitellopy import Tello


def inittello():
    drone = Tello()
    drone.connect()
    drone.streamon()

    return drone



def telloframe(drone, w=360, h=240):
    frame = drone.get_frame_read().frame
    img = cv2.cv2.resize(frame, (w, h))
    return img


def adjust(drone, vector):
    fb = 0
    if vector[2] >= 10:
        fb = -20
    elif vector[2] <= -10:
        fb = 20
    elif vector[2] > -10 or vector[2] < 10:
        fb = 0

    drone.send_rc_control(0,fb,-(int(vector[0])/10),0)
