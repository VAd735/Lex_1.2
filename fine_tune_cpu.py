
import os
# Перенаправляємо HF/transformers кеші на D: (щоб нічого не писалось на C:)
HF_BASE = os.environ.get("HF_HOME", r"D:\hf_cache")
os.environ["HF_HOME"] = HF_BASE
os.environ["TRANSFORMERS_CACHE"] = os.path.join(HF_BASE, "transformers")
os.environ["HF_DATASETS_CACHE"] = os.path.join(HF_BASE, "datasets")
os.environ["HF_MODULES_CACHE"] = os.path.join(HF_BASE, "modules")
os.environ["HF_METRICS_CACHE"] = os.path.join(HF_BASE, "metrics")
os.environ["XDG_CACHE_HOME"] = HF_BASE

from llama_cpp import Llama

# Вказуємо реальний абсолютний шлях до твоєї моделі на диску D:
MODEL_PATH = r"D:\Lex\models\qwen2.5-3b-instruct-q4_k_m.gguf"

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=4096,
    n_threads=6,
    verbose=True
)

print("🔥 Модель завантажена! Починаємо дообучення...\n")

# Читаємо твій data.txt
DATA_PATH = r"D:\Lex\data\Data.txt"
with open(DATA_PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Проходимося по лініях
for i, line in enumerate(lines):
    prompt = f" Навчися з цього прикладу: {line}\n Відповідай 'OK' якщо зрозумів."
    print(f"\n==== TRAINING {i+1}/{len(lines)} ====")
    
    output = llm(
        prompt,
        max_tokens=50,
        temperature=0.1,
        stop=["</s>"]
    )

    print(" AI:", output["choices"][0]["text"].strip())

print("\n 🎉🎉🎉 Тренування завершено. ")