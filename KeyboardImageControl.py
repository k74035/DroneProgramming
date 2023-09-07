from djitellopy import tello
import KeyBoardControl as kp
import cv2

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())

me.takeoff()
me.streamon()

def video_stream():
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360,240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)

while True:
    video_stream()
    vals = kp.getKeyboardInput()
    if vals[4] is not None:
        if vals[4] == 'land':
            me.land()
        elif vals[4] == 'takeoff':
            me.takeoff()
        elif vals[4] == 'flip_left':
            me.flip_left()
        elif vals[4] == 'flip_right':
            me.flip_right()
    else:
        me.send_rc_control(vals[0], vals[1], vals[2], vals[3])