from llama_cpp import Llama
import os

MODEL_PATH = "models/qwen2.5-3b-instruct-q4_k_m.gguf"

if not os.path.exists(MODEL_PATH):
    raise RuntimeError("Model file not found. Запусти download_model.py")

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=1024,
    n_threads=2
)

def generate_answer(text):
    result = llm(f"[INST] {text} [/INST]", max_tokens=150)
    return result["choices"][0]["text"].strip()

