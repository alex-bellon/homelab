import os, json
from datetime import datetime
from telegram.ext import (
    Updater,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    Filters,
)

PRINT = 0


def download_video(update, context):

    message = update.message
    text = message.text.replace("/dl ", "")
    sender = message.from_user

    success = os.system("youtube-dl -o '/media/alex/Media/YouTube/%(title)s' " + text)

    if success == 0:
        update.message.reply_text("Video successfully downloaded!")
    else:
        update.message.reply_text("Video did not download")


def print_intro(update, context):
    update.message.reply_text("Please send the text or image you want to print")
    return PRINT


def print_text(update, context):

    text = update.message.text

    os.system('echo "' + text + '" > print.txt')
    success = os.system("lp -d thermal-printer print.txt")

    if success == 0:
        update.message.reply_text("Text successfully printed!")
    else:
        update.message.reply_text("Text did not print :(")

    return ConversationHandler.END


def print_photo(update, context):

    image_list = update.message.photo
    image = image_list[0].get_file().download(custom_path="print")

    success = os.system("lp -d thermal-printer print")

    if success == 0:
        update.message.reply_text("Image successfully printed!")
    else:
        update.message.reply_text("Image did not print :(")

    return ConversationHandler.END


def cancel(update, context):
    return ConversationHandler.END


def main():
    token = open("telegram.token", "r").read().strip("\n")
    user = json.loads(open("creds.json", "r").read())["telegram"]["username"]

    updater = Updater(token, use_context=True)
    disp = updater.dispatcher

    disp.add_handler(CommandHandler("help", help))
    disp.add_handler(
        ConversationHandler(
            entry_points=[CommandHandler("print", print_intro)],
            states={
                PRINT: [
                    MessageHandler(Filters.text, print_text),
                    MessageHandler(Filters.photo, print_photo),
                ]
            },
            fallbacks=[CommandHandler("cancel", cancel)],
        )
    )

    disp.add_handler(
        CommandHandler(
            "dl", download_video, filters=Filters.user(username=user) & Filters.text
        )
    )

    updater.start_polling()
    updater.idle()


main()
