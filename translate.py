from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from googletrans import Translator


API_TOKEN = '6927805573:AAFCWHwiQ0-06HKaG_QUGn34uIKcO2B408Q'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I can translate English to Farsi. Send me a message in English.')

def translate_to_farsi(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    translator = Translator()
    translated_text = translator.translate(text, src='en', dest='fa').text
    update.message.reply_text(translated_text)

def main() -> None:
    updater = Updater(token=API_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, translate_to_farsi))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
