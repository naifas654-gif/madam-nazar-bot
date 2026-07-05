import os
import time
from flask import Flask
from threading import Thread
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters

app = Flask(__name__)
@app.route('/')
def home(): return "البوت يعمل!"

IMAGE_URL = "https://madamnazar.io/assets/nazar.jpg"

def handle_nazar_request(update, context):
    user_text = update.message.text.strip().lower()
    if user_text == "نزار" or user_text == "مدام نزار":
        final_url = f"{IMAGE_URL}?v={time.time()}"
        keyboard = [[InlineKeyboardButton("⏰ يتغير الموقع الساعة 09:02 صباحاً", callback_data='ignore')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_photo(
            photo=final_url,
            caption="تفضل هذا موقع مدام نزار اليوم 🔮🃏",
            reply_markup=reply_markup
        )

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    Thread(target=run).start()
    updater = Updater("8639550044:AAFV6yiRM6KEK3sv5QZHXXlVqReoPcuXoeI")
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_nazar_request))
    updater.start_polling()
    updater.idle()
