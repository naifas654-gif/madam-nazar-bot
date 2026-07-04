from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from flask import Flask
import threading
import requests

TOKEN = '8639550044:AAFV6yiRM6KEK3sv5QZHXXlVqReoPcuXoeI'
NAZAR_PHOTO_URL = "https://jeanropke.github.io/RDOMap/img/nazar_daily.jpg"

app_web = Flask(__name__)
@app_web.route('/')
def home(): return "Nazar Bot is active!"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if "نزار" in text or "مدام نزار" in text:
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(NAZAR_PHOTO_URL, headers=headers)
            
            await update.message.reply_photo(
                photo=response.content, 
                caption="تفضل هذا موقع مدام نزار اليوم 🔮🃏"
            )
        except Exception:
            await update.message.reply_text("عذراً، لم أستطع جلب الصورة حالياً، حاول مجدداً لاحقاً.")

if __name__ == '__main__':
    threading.Thread(target=lambda: app_web.run(host='0.0.0.0', port=8080)).start()
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
