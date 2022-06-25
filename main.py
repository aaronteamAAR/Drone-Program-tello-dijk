from djitellopy import tello
from time import sleep

us = tello.Tello()
us.connect()
print(us.get_battery())
us.takeoff()
us.move_forward(15)
sleep(2)
##After sleep move
us.send_rc_control(0, 50, 0, 0)
##left, right, forward, backward and yaw(twist of drone)
sleep(1)
us.send_rc_control(10, 0, 0, 0)
sleep(4)
us.send_rc_control(0, 0, 0, 0)
## so as to land like a helicopter
us.land()