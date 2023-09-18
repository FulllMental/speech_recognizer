import os

from dotenv import load_dotenv
import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Здравствуйте!')


def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)


def main(telegram_token) -> None:
    updater = Updater(telegram_token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    load_dotenv()
    telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
    main(telegram_token)
