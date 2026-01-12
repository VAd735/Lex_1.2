import os
import urllib.request

URL = "https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-GGUF/resolve/main/qwen2.5-3b-instruct-q4_k_m.gguf"

os.makedirs("models", exist_ok=True)
MODEL_PATH = "models/qwen3b.gguf"

if not os.path.exists(MODEL_PATH):
    print("Downloading model...")
    urllib.request.urlretrieve(URL, MODEL_PATH)
    print("Download finished.")
else:
    print("Model already exists.")
