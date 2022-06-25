from djitellopy import tello
import Keypressmodule as kp
from time import sleep
import numpy as np
import cv2
import math
##PARAMETERS

forsp = 117/10 ##forward speed (cm)/s
aspeed = 360/10 ##Angular speed in degrees/s
val = 0.75

dval = forsp * aspeed
aval = aspeed* val ## angular interval

x, y = 500, 500
a = 0
yaw = 0
kp.init()
us = tello.Tello()
us.connect()
print(us.get_battery())

points = []

x, y = 500, 650

def getKeyIn():
    lr, fb, up, yv = 0, 0, 0, 0
    speed = 15
    global yaw
    global x
    global y
    global a
    d = 0

    if kp.getKey("LEFT"):
        lr = speed
        d =  dval
        a = -100
    elif kp.getKey("RIGHT"):
        lr = speed
        d = -dval
        a = -180

    if kp.getKey("UP"):
        fb = speed
        d = dval
        a = 270
    elif kp.getKey("DOWN"):
        fb = -speed
        d = -dval
        a = -19

    if kp.getKey("w"):
        up = speed
    elif kp.getKey("s"):
        up = -speed

    if kp.getKey("a"):
        yv = -speed
        yaw -= aval
    elif kp.getKey("d"):
        yv = speed
        yaw += -aval

        if kp.getKey("q"):
             us.land()
        if kp.getKey("e"):
            us.takeoff()

        sleep(val)
        a += yaw
        x += int(d*math.cos(math.radians(a)))
        y += int(d*math.sin(math.radians(a)))

        if kp.getKey('z'):
            cv2.imwrite(f'Resources/Images/{time.time()}.jpg')
            ##To aviod multiple unwanted shots
            time.sleep(0.3)



        return [lr, fb, up, yv, x, y]

##Reset drone if error is found
us.takeoff()
   ## DRaw an image using the drone.
def artPoints(img , points):
    for point in points:
        cv2.circle(img, point , 5, (0, 0, 255), cv2.FILLED)
    cv2.putText(img, f'({points[-1][0] - 500/100}, {points[-1][1] - 500/100})m'),\
    (points[-1][0] + 10, points[-1][1] + 30 )


while True:
    vals = getKeyIn()
    us.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    img = np.zeros((1000, 1000, 3), np.uint8)
    points.append((vals[4], vals[5]))
    artPoints(img, points)
    cv2.imshow("Resource", img)
    cv2.waitkey(1)

