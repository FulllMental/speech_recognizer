import logging
import os

import telegram
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from dialogflow_handler import detect_intent_texts


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Здравствуйте!')


def reply(update: Update, context: CallbackContext) -> None:
    project_id = os.getenv('PROJECT_ID')
    session_id = update.effective_user
    text = update.message.text
    answer = detect_intent_texts(project_id, session_id, text, 'ru')
    if not answer['is_fallback']:
        update.message.reply_text(answer['fulfillment_text'])
    else:
        update.message.reply_text('К сожалению, я не понимаю вас...')


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
    )
    logger = logging.getLogger(__name__)
    load_dotenv()
    telegram_token = os.getenv('TG_BOT_TOKEN')
    tg_user_id = os.getenv('TG_USER_ID')
    try:
        updater = Updater(telegram_token)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler('start', start))
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))
        updater.start_polling()
        updater.idle()
    except Exception as err:
        error_text = 'Telegram_Bot stopped working with an error...'
        bot = telegram.Bot(token=telegram_token)
        bot.send_message(chat_id=tg_user_id, text=error_text)
