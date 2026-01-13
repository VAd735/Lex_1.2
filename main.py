from flask import Flask, request
import os
from telegram import Bot, Update
from telegram.ext import Dispatcher, MessageHandler, filters
from model import generate_answer  # твоя функція для відповіді

app = Flask(__name__)

TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN)

# Telegram Dispatcher для обробки повідомлень
dispatcher = Dispatcher(bot, None, workers=0)

# Обробник текстових повідомлень
def handle_message(update: Update, context):
    text = update.message.text
    answer = generate_answer(text)
    update.message.reply_text(answer)

dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

@app.route("/", methods=["GET"])
def home():
    return "Bot is running!"

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "OK"

if __name__ == "__main__":
    # На Railway просто запуск Flask
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
