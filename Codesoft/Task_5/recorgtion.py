import tkinter as tk
from tkinter import messagebox
import cv2
import face_recognition
import os
import numpy as np

# Load known faces
known_face_encodings = []
known_face_names = []

def load_known_faces():
    folder = "known_faces"
    for filename in os.listdir(folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image = face_recognition.load_image_file(os.path.join(folder, filename))
            encoding = face_recognition.face_encodings(image)
            if encoding:
                known_face_encodings.append(encoding[0])
                known_face_names.append(os.path.splitext(filename)[0])
            else:
                print(f"⚠ No face found in {filename}")

# Start webcam and detect/recognize faces
def start_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Error", "Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            name = "Unknown"
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)

            if matches:
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

        cv2.imshow("Face Detection & Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# GUI setup
def start_app():
    load_known_faces()
    start_camera()

root = tk.Tk()
root.title("Face Detection & Recognition")
root.geometry("300x150")

tk.Label(root, text="Face Recognition System", font=("Arial", 14)).pack(pady=10)
tk.Button(root, text="Start Camera", command=start_app, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 12)).pack(pady=5)

root.mainloop()