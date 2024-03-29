# Распознователь речи

Данный репозиторий представляет собой диалогового бота, позволяющего распознавать текст в свободной форме и отвечать на
вопросы одним из заготовленных ответов через Telegram:

![tg_bot_2](https://github.com/FulllMental/speech_recognizer/assets/104234625/6290ca16-dba2-4b8f-94c6-bd15679273bc)


и/или через VK:


![vk_bot](https://github.com/FulllMental/speech_recognizer/assets/104234625/ebaf8abe-3c4b-4a87-afba-f751371557c9)


## Запуск локально

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. Установите зависимости:

```sh
pip install -r requirements.txt
```
Залогиньтесь gcloud auth application-default login

- Создайте новый проект на [Dialogflow](https://dialogflow.cloud.google.com)
- Создайте [агента](https://cloud.google.com/dialogflow/es/docs/quick/build-agent) для DialogFlow 
- Добавьте необходимые фразы (Intents) на которые должен реагировать бот
- Установите на сервер [cloud.google.cli](https://cloud.google.com/sdk/docs/install#deb) и выберете нужный проект
- Залогиньтесь 
```sh
gcloud auth application-default login
```
- Запустите бота


для запуска Telegram бота:
```sh
python telegram_bot.py
```
для запуска VK бота:
```sh
python vk_bot.py
```

## Переменные окружения

Для запуска бота вам необходимо его зарегистрировать его у [Отца ботов](https://telegram.me/BotFather)

Для VK вам необходимо в настройках вашего сообщества получить ключ API во вкладке "Работа с API" 

Доступные переменные:
- `TG_BOT_TOKEN` — Уникальный ключ для привязки к вашему боту
- `VK_GROUP_TOKEN` — Токен для доступа бота к сообщениям вашего сообщества в VK
- `PROJECT_ID` — ID вашего проекта на [Dialogflow](https://dialogflow.cloud.google.com)
- `TG_USER_ID` - ID вашего профиля в Telegram для получения сообщений о ошибках бота (можно узнать [тут](https://t.me/getmyid_bot))
- `NEW_PHRASES_JSON` - Путь до `.json` файла с фразами для обучения DialogFlow

Для запуска обучения из файла, после присвоения всех значений, запустите скрипт:
```sh
python add_intents.py
```

## Цели проекта

Код написан в учебных целях — для курса по Python и веб-разработке на сайте [Devman](https://dvmn.org).
