import tensorflow as tf
import numpy as np
import cv2

interpreter = tf.lite.Interpreter(model_path="models/eye_model.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def predict_eye_state(eye_crop):
    img = cv2.resize(eye_crop, (96, 96)) / 255.0
    img = np.expand_dims(img, axis=0).astype(np.float32)
    interpreter.set_tensor(input_details[0]['index'], img)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_details[0]['index'])[0]
    return "closed" if preds[1] > 0.5 else "open"
