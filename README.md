# Распознователь речи

Данный репозиторий представляет собой диалогового бота, позволяющего распознавать текст в свободной форме и отвечать на
вопросы одним из заготовленных ответов с использованием Telegram:

<img src="https://media.giphy.com/media/qriDL5mF5l2aFyQSqp/giphy.gif" width="350" height="400" />

и/или Vk:

<img src="https://media4.giphy.com/media/eY26j2qp39tnP7LwCu/giphy.gif" width="350" height="400" />
## Запуск локально

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. Установите зависимости:

```sh
pip install -r requirements1.txt
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
