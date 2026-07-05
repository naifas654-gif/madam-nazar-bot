import os
import time
from flask import Flask
from threading import Thread
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

app = Flask(__name__)
@app.route('/')
def home(): return "البوت يعمل!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.strip().lower()
    if user_text == "نزار" or user_text == "مدام نزار":
        keyboard = [[InlineKeyboardButton("⏰ يتغير الموقع الساعة 09:02 صباحاً", callback_data='ignore')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_photo(
            photo="https://madamnazar.io/assets/nazar.jpg",
            caption="تفضل هذا موقع مدام نزار اليوم 🔮🃏",
            reply_markup=reply_markup
        )

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))

if __name__ == '__main__':
    Thread(target=run).start()
    app_bot = ApplicationBuilder().token("8639550044:AAFV6yiRM6KEK3sv5QZHXXlVqReoPcuXoeI").build()
    app_bot.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), start))
    app_bot.run_polling()
