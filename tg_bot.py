from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes


TOKEN = "8685417658:AAGH4OKHOv3rax106gum5xERvQWvplif7Uc"
def chat(messe):
    count=0
    if messe=="привет":
        return "как дела?"
        count=count+1
    elif messe=="как дела?":
        return "нормально"
        count=count+1
    elif messe=="ты супер":
        return "ты тоже супер"
        count=count+1
    elif messe=="мы друзья ?":
        return "конечно,"
        count=count+1
    elif messe=="пока":
        return str(count)
    elif messe=="помощь":
        return "привет я умею: \n здороваться \n делать комплементы \n прощаться"
    else:
        return "я тебя не понимаю"
        count=count+1

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "Привет! Напиши мне что-нибудь."
    )


async def answer_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    message = update.message.text.lower()

    answer = chat (message)

    await update.message.reply_text(answer)


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        answer_message
    )
)

app.run_polling()

