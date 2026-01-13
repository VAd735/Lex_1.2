from flask import Flask
from threading import Thread
import os
import download_model


from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

from model import generate_answer

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    answer = generate_answer(text)
    await update.message.reply_text(answer)

def start_bot():
    TOKEN = os.getenv("TOKEN")
    app_tg = ApplicationBuilder().token(TOKEN).build()
    app_tg.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    app_tg.run_polling()

if __name__ == "__main__":
    Thread(target=start_bot).start()

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
