"""
Microsleep Cloud App Package
--------------------------------
Berisi modul utama untuk sistem deteksi microsleep berbasis cloud:
- main.py         → FastAPI server
- model_eye.py    → Model TFLite untuk deteksi mata (open/close)
- model_mouth.py  → Model ONNX untuk deteksi mulut (yawn/no-yawn)
- mediapipe_utils.py → Ekstraksi landmark wajah (mata & mulut)
- logic.py        → Logika keputusan akhir
"""

__version__ = "1.0.0"
