import cv2
import time

def findFace(img):
    faceCascade = cv2.CascadeClassifier("models/haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)

    myFaceListC = []
    myFaceListArea = []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cx = x + w // 2
        cy = y + h // 2
        area = w * h
        cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        myFaceListC.append([cx,cy])
        myFaceListArea.append(area)
    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea)) # 카메라를 통해 얻은 얼굴 값(리스트)중 그 면적이 제일 큰, 즉 제일 가까운 얼굴
        return img, [myFaceListC[i],myFaceListArea[i]]
    else:
        return img, [[0, 0], 0]

def trackFace(me, info, w, pid, pError):


cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    img, info = findFace(img)
    print("Center", info[0], "Area", info[1]) # info의 1번쨰 인덱스, 즉 가장 가까운 얼굴의 면적 값
    cv2.imshow("OutPut", img)
    cv2.waitKey(1)