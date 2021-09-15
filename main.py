from djitellopy import tello
import time


drone = tello.Tello()
drone.connect()
print(drone.get_battery())
drone.takeoff()
time.sleep(10)
drone.land()



