import os
import random

import telegram
import vk_api
from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType

from dialogflow_handler import detect_intent_texts


def reply(event, project_id, vk_api):
    answer = detect_intent_texts(project_id, event.user_id, event.text, 'ru')
    if not answer['is_fallback']:
        vk_api.messages.send(
            user_id=event.user_id,
            message=answer['fulfillment_text'],
            random_id=random.randint(1, 1000)
        )


if __name__ == '__main__':
    load_dotenv()
    vk_group_token = os.getenv('VK_GROUP_TOKEN')
    telegram_token = os.getenv('TG_BOT_TOKEN')
    project_id = os.getenv('PROJECT_ID')
    tg_user_id = os.getenv('TG_USER_ID')
    try:
        vk_session = vk_api.VkApi(token=vk_group_token)
        vk_api = vk_session.get_api()
        longpoll = VkLongPoll(vk_session)
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                reply(event, project_id, vk_api)
    except Exception as err:
        error_text = 'VK_Bot stopped working with an error...'
        bot = telegram.Bot(token=telegram_token)
        bot.send_message(chat_id=tg_user_id, text=error_text)
