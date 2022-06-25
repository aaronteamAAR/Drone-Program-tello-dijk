from djitellopy import tello
import Keypressmodule as kp
import time
import cv2

kp.init()
us = tello.Tello()
us.connect()
print(us.get_battery())


def getKeyIn():
    lr, fb, up, yv = 0, 0, 0, 0
    speed = 50
    if kp.getKey("LEFT"): lr = speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"):
        fb = speed
    elif kp.getKey("DOWN"):
        fb = -speed

    if kp.getKey("w"):
        up = speed
    elif kp.getKey("s"):
        up = -speed

    if kp.getKey("a"):
        yv = -speed
    elif kp.getKey("d"):
        yv = speed

        if kp.getKey("q"):
             us.land()
        if kp.getKey("e"):
            us.takeoff()

        if kp.getKey('z'):
            cv2.imwrite(f'Resources/Images/{time.time()}.jpg')
            ##To aviod multiple unwanted shots
            time.sleep(0.3)

        return [lr, fb, up, yv ]

##Reset drone if error is found
us.takeoff()

while True:
    vals = getKeyIn()
    us.send_rc_control(vals[0], vals[1], vals[2], vals[3])

