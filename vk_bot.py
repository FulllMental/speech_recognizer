import os
import random

import vk_api
from dotenv import load_dotenv
from google.cloud import dialogflow
from vk_api import exceptions
from vk_api.longpoll import VkLongPoll, VkEventType


def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = {'text': text, 'language_code': language_code}
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )
    return response.query_result.fulfillment_text


def reply(event, project_id, vk_api):
    try:
        answer = detect_intent_texts(project_id, event.user_id, event.text, 'en-US')
        vk_api.messages.send(
            user_id=event.user_id,
            message=answer,
            random_id=random.randint(1, 1000)
        )
    except exceptions.VkApiError:
        pass


if __name__ == '__main__':
    load_dotenv()
    vk_group_token = os.getenv('VK_GROUP_TOKEN')
    project_id = os.getenv('PROJECT_ID')

    vk_session = vk_api.VkApi(token=vk_group_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            reply(event, project_id, vk_api)
