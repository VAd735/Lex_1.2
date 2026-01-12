from flask import Flask
import download_model
from model import generate_answer
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from threading import Thread
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply = generate_answer(update.message.text)
    await update.message.reply_text(reply)

def start_telegram_bot():
    TOKEN = os.getenv("TOKEN")
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    application.run_polling()

if __name__ == "__main__":
    # запускаємо Telegram у фоновому потоці
    Thread(target=start_telegram_bot).start()
    # Flask сервер для Railway
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
