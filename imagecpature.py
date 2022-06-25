from djitellopy import tello
import cv2

us = tello.Tello()
us.connect()
print(us.get_battery())

us.streamon()

while True:
    pic = us.get_frame_read().frame
    pic = cv2.resize(pic, (360, 240))
    pic.imshow("image", pic)
    cv2.waitKey(2)