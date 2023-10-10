import cv2
import torch

# Load the custom YOLOv5 model
model = torch.hub.load('C://Users//k7403//Desktop//ProjectPython//yolov5-master', 'custom', path='best.pt', source='local')

cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()
    
    # Perform inference on the frame
    results = model(frame)
    
    # Get detected faces
    detected_faces = results.pred[0]
    
    # Create an empty list to store face coordinates
    face_coordinates = []
    
    for face in detected_faces:
        x1, y1, x2, y2, conf, cls = face.tolist()
        
        # Add face coordinates to the list
        face_coordinates.append((x1, y1, x2, y2))
        
        # Draw bounding box on the frame
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
    
    # Display the frame
    cv2.imshow("YOLOv5", frame)

    # Print the coordinates of detected faces
    print("Detected Face Coordinates:")
    for i, coords in enumerate(face_coordinates):
        print(f"Face {i + 1}: x1={coords[0]}, y1={coords[1]}, x2={coords[2]}, y2={coords[3]}")

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
