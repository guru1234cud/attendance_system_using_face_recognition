import cv2
from face_recognition_module import FaceRecognitionSystem
from attendance_module import AttendanceSystem

def main():
    face_recog = FaceRecognitionSystem()
    attendance_sys = AttendanceSystem()

    # Load previous attendance
    attendance_sys.load_attendance()

    # Capture video feed
    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        # Recognize faces
        face_locations, names = face_recog.recognize_face(frame)

        # Draw rectangles around faces and display names
        for (top, right, bottom, left), name in zip(face_locations, names):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            # Mark attendance
            if name != "Unknown":
                attendance_sys.mark_attendance(name)

        # Display the resulting frame
        cv2.imshow('Attendance System', frame)

        # Break the loop on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
