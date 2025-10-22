import onnxruntime as ort
import numpy as np
import cv2

session = ort.InferenceSession("models/mouth_model.onnx")

def predict_mouth_state(mouth_crop):
    img = cv2.resize(mouth_crop, (128, 128)) / 255.0
    img = np.transpose(img, (2, 0, 1))[None, :, :, :].astype(np.float32)
    output = session.run(None, {"input": img})[0]
    label = np.argmax(output)
    return "yawn" if label == 1 else "no_yawn"
