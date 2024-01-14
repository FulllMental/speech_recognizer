import os
import json

from dotenv import load_dotenv
from google.cloud import dialogflow


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    '''Create an intent of the given intent type.'''
    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:  # questions
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )

    response = intents_client.create_intent(
        parent=parent, intent=intent, language_code='ru'
    )

    print('Intent created: {}'.format(response))


if __name__ == '__main__':
    load_dotenv()
    project_id = os.getenv('PROJECT_ID')
    new_phrases = os.getenv('NEW_PHRASES_JSON')
    with open(new_phrases, 'r', encoding='utf-8') as new_phrases:
        phrases = new_phrases.read()
    all_phrases = json.loads(phrases)

    for phrase_type, training_phrases_parts in all_phrases.items():
        questions, answers = training_phrases_parts.values()
        create_intent(project_id, phrase_type, questions, list(answers))
