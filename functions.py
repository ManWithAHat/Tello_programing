import cv2.cv2
from djitellopy import Tello


def inittello():
    drone = Tello()
    drone.connect()
    drone.set_speed_x(0)
    drone.set_speed_y(0)
    drone.set_speed_z(0)
    drone.streamon()
    return drone

def telloframe(drone,w = 360,h = 240):
    frame = drone.get_frame_read().frame
    img = cv2.cv2.resize(frame,(w,h))
    return img

