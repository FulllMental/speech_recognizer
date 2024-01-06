import os

from dotenv import load_dotenv
import logging

from telegram import Update, error
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from google.cloud import dialogflow


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Здравствуйте!')


def reply(update: Update, context: CallbackContext) -> None:
    project_id = os.getenv('PROJECT_ID')
    session_id = update.effective_user
    text = update.message.text
    try:
        answer = detect_intent_texts(project_id, session_id, text, 'en-US')
        update.message.reply_text(answer)
    except error.BadRequest:
        update.message.reply_text('К сожалению, я не понимаю вас...')


def main(telegram_token) -> None:
    updater = Updater(telegram_token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))
    updater.start_polling()
    updater.idle()


def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = {'text': text, 'language_code': language_code}
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(
        request={'session': session, 'query_input': query_input}
    )
    return response.query_result.fulfillment_text


if __name__ == '__main__':
    load_dotenv()
    telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
    main(telegram_token)
