from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OWNER_CHAT_ID = os.getenv("OWNER_CHAT_ID")
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
        context.user_data["step"]="phone"
        await update.message.reply_text(
        "для заказа напишите номер телефона",
    )
    elif step=="phone":
        context.user_data["phone"]=message
        context.user_data["step"]="zakaz"
        keyboard=[["манная каша","борщ"],["котлета говяжья","котлета куринная"],["картока фри","варенная картошка"]]
        reply_markup = ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )
        name=context.user_data["name"]
        phone=context.user_data["phone"]
        await update.message.reply_text(
            f"Приятно познакомиться, {name}, ваш номер телефона {phone}!\n"
            "что будете заказывать ?",
            reply_markup=reply_markup
        )
    elif step=="zakaz":
        context.user_data["zakaz"]=message
        zakaz=context.user_data["zakaz"]
        context.user_data["step"]="true"
        keyboard=[["да","нет"]]
        reply_markup = ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )
        name=context.user_data["name"]
        phone=context.user_data["phone"]
        await update.message.reply_text(
            f"ваш заказ:\n"
            f"ваше имя: {name}\n"
            f"ваш номер телефона: {phone}\n"
            f"ваш заказ: {zakaz}\n"
            f"верно ?",
            reply_markup=reply_markup
        )
    elif step=="true":
        otvet=message
        if otvet=="да":
            keyboard=[["что-то еще ?","заказ готов"]]
            reply_markup = ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
            ) 
            await update.message.reply_text("выберите:",reply_markup=reply_markup)
            name=context.user_data["name"]
            phone=context.user_data["phone"]
            zakaz=context.user_data["zakaz"]
            await context.bot.send_message(
                chat_id=OWNER_CHAT_ID,
                text=(
                 "заказ:\n"
                 f"имя: {name}\n"
                 f"номер телефона: {phone}\n"
                 f"заказ: {zakaz}\n")
            )
        
        elif otvet=="что-то еще ?":
            context.user_data.clear()
            context.user_data["step"]="name"
            await update.message.reply_text(
                f"давай начнем сначало: \n"
                f"как тебя зовут ?",  
                reply_markup=reply_markup
            )
        elif otvet=="заказ готов":
            await update.message.reply_text("хорошо,ожидайте")
        elif otvet=="нет":
            context.user_data.clear()
            context.user_data["step"]="name"
            await update.message.reply_text(
                f"давай начнем сначало: \n"
                f"как тебя зовут ?",  
                reply_markup=reply_markup
            )
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

