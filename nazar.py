import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if "نزار" in text or "مدام نزار" in text:
        image_url = "https://raw.githubusercontent.com/jeanropke/RDOMap/master/nazar.png"
        message_text = "تفضل، هذا موقع مدام نزار اليوم."
        
        keyboard = [[InlineKeyboardButton("يتغير الموقع الساعة 9:02 صباحاً", callback_data='ignore')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_photo(photo=image_url, caption=message_text, reply_markup=reply_markup)

if __name__ == '__main__':
    app_bot = ApplicationBuilder().token("8639550044:AAFV6yiRM6KEK3sv5QZHXXlVqReoPcuXoeI").build()
    
    app_bot.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    app_bot.run_polling()
