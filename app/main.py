from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from app.model_eye import predict_eye_state
from app.model_mouth import predict_mouth_state
from app.mediapipe_utils import extract_eye_mouth
from app.logic import decide_state
import cv2, numpy as np

app = FastAPI(title="Microsleep Detection Cloud API")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # === 1️⃣ Baca frame dari ESP32 ===
        img_bytes = await file.read()
        np_arr = np.frombuffer(img_bytes, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # === 2️⃣ Crop area mata & mulut pakai Mediapipe ===
        eye_crop, mouth_crop = extract_eye_mouth(frame)

        # === 3️⃣ Prediksi dua model ===
        eye_state = predict_eye_state(eye_crop)
        mouth_state = predict_mouth_state(mouth_crop)

        # === 4️⃣ Logika akhir ===
        result = decide_state(eye_state, mouth_state)

        return JSONResponse({
            "eye": eye_state,
            "mouth": mouth_state,
            "status": result
        })

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


@app.get("/")
def home():
    return {"message": "Microsleep Detection API is running"}
