from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
from answer import chat 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["step"] = "name"
    await update.message.reply_text(
        "Привет! как тебя зовут ?",
    )



async def answer_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    message = update.message.text.lower()
    step=context.user_data["step"]
    if step=="name":
        context.user_data["name"]=message
        context.user_data["step"]="zakaz"
        keyboard=[["манная каша","борщ"],["котлета говяжья","котлета куринная"],["картока фри","варенная картошка"]]
        reply_markup = ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )
    
        await update.message.reply_text(
            f"Приятно познакомиться, {message}!\n"
            "что будете заказывать ?",
            reply_markup=reply_markup
        )
    elif step=="zakaz":
        context.user_data["zakaz"]=message
        await update.message.reply_text("заказ принят, ожидайте")
    else:
         await update.message.reply_text("я тебя не понимаю")
        
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        answer_message
    )
)

app.run_polling()

