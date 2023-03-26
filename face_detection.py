import cv2
import numpy as np
from deepface import DeepFace

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initialize the video capture object
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    _, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Loop through each face and detect its age, gender, and expression
    for (x, y, w, h) in faces:
        # Extract the face ROI
        face_img = frame[y:y + h, x:x + w].copy()

        # print(face_img)

        # Get the age, gender, and facial expression of the face using DeepFace
        detected_face = DeepFace.analyze(face_img, enforce_detection=False)

        # print(detected_face[0]['gender'])

        # Check if the detected_face object is a dictionary
        # if isinstance(detected_face, dict):
        age = int(detected_face[0]['age'])
        gender = detected_face[0]['gender']
        expression = detected_face[0]['dominant_emotion']
        race = detected_face[0]['race']
        print(gender)

        # Draw a rectangle around the face and display the age, gender, and expression
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, f"Age: {age}", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, f"Gender: {gender}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, f"Expression: {expression}", (x, y + h + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, f"Race: {race}", (x, y + h + 46), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()