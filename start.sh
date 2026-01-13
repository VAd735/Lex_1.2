#!/bin/bash
# Встановлюємо libgomp для llama_cpp
apt-get update && apt-get install -y libgomp1

# Запускаємо віртуальне оточення та скрипт
source .venv/bin/activate
python main.py
