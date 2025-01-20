import cv2
import face_recognition
import numpy as np
import os

class FaceRecognitionSystem:
    def __init__(self, images_path="C:\\Users\\GURU\\Desktop\\attendance system\\images"):
        self.known_encodings = []
        self.known_names = []
        self.images_path = images_path
        self.load_known_faces()

    def load_known_faces(self):
        # Load known faces from the images folder
        image_files = os.listdir(self.images_path)
        for image_file in image_files:
            img = cv2.imread(f"{self.images_path}/{image_file}")
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encoding = face_recognition.face_encodings(rgb_img)[0]
            self.known_encodings.append(encoding)
            self.known_names.append(os.path.splitext(image_file)[0])
    def recognize_face(self, frame):
        # Convert the frame to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Detect face locations and encodings in the current frame
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(self.known_encodings, face_encoding)
            face_distances = face_recognition.face_distance(self.known_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = self.known_names[best_match_index]
            else:
                name = "Unknown"
            
            names.append(name)

        return face_locations, names
