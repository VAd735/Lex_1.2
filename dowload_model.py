import os
import urllib.request

MODEL_URL = "https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct-GGUF/resolve/main/qwen2.5-1.5b-instruct-q4_k_m.gguf"
MODEL_PATH = "model.gguf"

def ensure_model():
    if os.path.exists(MODEL_PATH):
        print("Model already exists")
        return

    print("Downloading model (1.5B)...")
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
    print("Model downloaded!")
