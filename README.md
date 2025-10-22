<p align="center">
  <img src="https://media.giphy.com/media/IwTWTsUzmIicM/giphy.gif" width="200"/>
</p>

<h1 align="center">🚗 EyeGuard Cloud API — Sistem Deteksi Microsleep Realtime</h1>

<p align="center">
  <b>Deteksi Kantuk dan Menguap secara Real-time menggunakan Deep Learning + MediaPipe + Render Cloud</b><br/>
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/TensorFlow-TFLite-orange?logo=tensorflow&logoColor=white"/>
  <img src="https://img.shields.io/badge/ONNX-Runtime-green?logo=onnx&logoColor=white"/>
  <img src="https://img.shields.io/badge/FastAPI-Render%20Cloud-purple?logo=fastapi&logoColor=white"/>
</p>

---

## 🎥 **Demo Sistem**
<p align="center">
  <img src="https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif" width="600"/>
  <br/>
  <i>ESP32-CAM mengirim gambar → API Render mendeteksi kondisi mata & mulut → hasil dikirim kembali (Normal, Yawning, Microsleep)</i>
</p>

---

## 🧠 **Deskripsi Singkat**
**EyeGuard Cloud API** adalah sistem cerdas berbasis *Deep Learning* yang mampu mendeteksi tanda-tanda kantuk (*microsleep*) dan menguap secara **real-time**.

Sistem ini dibangun menggunakan dua model ringan:
- 👁️ **Model Mata (MobileNetV3-Small, TFLite)** — mendeteksi kondisi mata terbuka atau tertutup  
- 👄 **Model Mulut (EfficientNet-B0, ONNX)** — mengenali apakah pengguna sedang menguap atau tidak  
- 🧭 **MediaPipe FaceMesh** — mengekstraksi area mata dan mulut secara otomatis dari wajah  
- ⚙️ **FastAPI di Render Cloud** — sebagai server inferensi yang menerima input dari kamera (ESP32-CAM)

---

## ⚙️ **Arsitektur Sistem**
ESP32-CAM → Cloud (FastAPI di Render)
├── MediaPipe FaceMesh (crop ROI)
├── Model Mata (MobileNetV3-Small)
├── Model Mulut (EfficientNet-B0)
├── Decision Logic (Normal / Yawning / Microsleep)
└── JSON Output → {"eye":"closed", "mouth":"no_yawn", "state":"MICROSLEEP"}
<p align="center">
  <img src="https://media.giphy.com/media/l3vR85PnGsBwu1PFK/giphy.gif" width="550"/>
</p>

---

## 🧩 **Struktur Folder**
microsleep-cloud/
│
├── app/
│ ├── main.py # Server FastAPI utama
│ ├── model_eye.py # Model TFLite untuk deteksi mata
│ ├── model_mouth.py # Model ONNX untuk deteksi mulut
│ ├── mediapipe_utils.py # Ekstraksi mata & mulut dengan MediaPipe
│ ├── logic.py # Logika keputusan akhir
│ └── requirements.txt
│
├── models/
│ ├── eye_model.tflite
│ └── mouth_model.onnx
│
├── render.yaml # Konfigurasi Render Cloud
├── runtime.txt # Versi Python
└── README.md
