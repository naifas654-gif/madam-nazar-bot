import os
from flask import Flask, request
from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "8639550044:AAFV6yiRM6KEK3sv5QZHXXlVqReoPcuXoeI"
app = Flask(__name__)
application = Application.builder().token(TOKEN).build()

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if "نزار" in text or "مدام نزار" in text:
        message_text = (
            "📍 موقع مدام نزار لهذا اليوم:\n\n"
            "⏰ يتغير الموقع في تمام الساعة 09:02 صباحاً بتوقيت مكة المكرمة."
        )
        
        keyboard = [[InlineKeyboardButton("اضغط هنا لفتح الخريطة 🗺️", url="https://jeanropke.github.io/RDOMap/")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(message_text, reply_markup=reply_markup)

application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

@app.route('/', methods=['POST'])
def webhook():
    return "Bot is running"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

