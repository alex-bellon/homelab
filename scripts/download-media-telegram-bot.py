import os, json
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def help(update, context):
    
    update.message.reply_text('Send a YouTube link to have it downloaded!')

def download_video(update, context):
   
    message = update.message
    text = message.text
    sender = message.from_user
    
    success = os.system('youtube-dl -o \'~/Videos/%(title)s\' ' + text)
    success = os.system('youtube-dl -o \'/media/alex/Media/YouTube/%(title)s\' ' + text)

    if success == 0:
        update.message.reply_text('Video successfully downloaded!')
    else:
        update.message.reply_text('Video did not download')

def main():
    token = open('media_bot.token', 'r').read().strip('\n')
    user = json.loads(open('creds.json', 'r').read())['telegram']['username']
    updater = Updater(token, use_context=True)

    disp = updater.dispatcher

    disp.add_handler(CommandHandler('help', help, Filters.user(username=user)))
    disp.add_handler(MessageHandler(Filters.text, download_video, Filters.user(username=user)))

    updater.start_polling()
    updater.idle()

main()
