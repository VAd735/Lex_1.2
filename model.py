from llama_cpp import Llama
import os
from download_model import ensure_model

MODEL_PATH = "model.gguf"

ensure_model()

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_threads=4
)

def generate_answer(text: str) -> str:
    output = llm(
        f"[INST] {text} [/INST]",
        max_tokens=200,
        temperature=0.7,
        stop=["</s>"]
    )
    return output["choices"][0]["text"].strip()
