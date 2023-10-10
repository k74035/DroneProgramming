import cv2
import numpy as np
from djitellopy import tello
import time

me = tello.Tello()
me.connect()
print(me.get_battery())

me.streamon()
me.takeoff()
# me.send_rc_control(0, 0, 10, 0)
time.sleep(2.2)

w, h = 360, 240
fbRange = [6200, 6800]
pid = [0.4, 0.4, 0]
pError = 0

def findFaceYOLO(img, model):
    # Perform inference on the frame
    results = model(img)

    # Get detected faces
    faces = results.pred[0]

    myFaceListC = []
    myFaceListArea = []

    for face in faces:
        x1, y1, x2, y2, conf, cls = face.tolist()
        x, y = (x1 + x2) // 2, (y1 + y2) // 2
        area = (x2 - x1) * (y2 - y1)

        # Draw bounding box and center point
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.circle(img, (x, y), 5, (0, 255, 0), cv2.FILLED)

        myFaceListC.append([x, y])
        myFaceListArea.append(area)

    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListC[i], myFaceListArea[i]]
    else:
        return img, [[0, 0], 0]

# ...

while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img, (w, h))
    
    # Use the YOLOv5 model to find faces
    img, info = findFaceYOLO(img, model)
    
    pError = trackFace(info, w, pid, pError)
    
    cv2.imshow("OutPut", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        me.land()
        break
