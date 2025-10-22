import cv2
import mediapipe as mp

mp_face = mp.solutions.face_mesh

def extract_eye_mouth(frame):
    with mp_face.FaceMesh(static_image_mode=True, max_num_faces=1) as face_mesh:
        h, w, _ = frame.shape
        results = face_mesh.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if not results.multi_face_landmarks:
            return frame, frame  # fallback

        landmarks = results.multi_face_landmarks[0].landmark

        # Ambil ROI mata (kiri-kanan)
        eye_y = int(landmarks[159].y * h)
        eye_x = int(landmarks[33].x * w)
        eye_crop = frame[eye_y-30:eye_y+30, eye_x-40:eye_x+40]

        # Ambil ROI mulut
        mouth_y = int(landmarks[13].y * h)
        mouth_x = int(landmarks[78].x * w)
        mouth_crop = frame[mouth_y-40:mouth_y+40, mouth_x-60:mouth_x+60]

        return eye_crop, mouth_crop
