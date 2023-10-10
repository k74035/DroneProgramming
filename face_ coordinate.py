import cv2
import torch
import numpy as np

# Load YOLOv5 model
# load()에 매개변수로 'yolov5 폴더 저장된 위치', 'custom', path = 'train된 모델', source = 'local' 순으로 와야한다.
model = torch.hub.load('C://Users//k7403//Desktop//ProjectPython//yolov5-master', 'custom', path ='models/best.pt', source='local')

myFaceListC = []
myFaceListArea = []

# Open a webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    # Perform object detection with the YOLOv5 model
    results = model(frame)
    
    # Get detected objects
    detected_objects = results.pred[0]
    
    for obj in detected_objects:
        # Extract bounding box coordinates
        x1, y1, x2, y2, conf, cls = obj.tolist()
        
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2
        area = (x2-x1) * (y2-y1)
        
        # Draw a rectangle around the detected object
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        
        # Calculate and print the center coordinates

        print(f"Object center coordinates: ({center_x}, {center_y})")
        myFaceListC.append([center_x,center_y])
        myFaceListArea.append(area)
        
        if len(myFaceListArea) != 0:
            i = myFaceListArea.index(max(myFaceListArea)) # 카메라를 통해 얻은 얼굴 값(리스트)중 그 면적이 제일 큰, 즉 제일 가까운 얼굴
            return img, [myFaceListC[i],myFaceListArea[i]]
        else:
            return img, [[0, 0], 0]

    # Display the frame with bounding boxes
    cv2.imshow("Object Detection", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
