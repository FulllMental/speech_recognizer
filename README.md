# Распознователь речи

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

Чтобы обучить бота фразам из `.json` файла добавьте в корневой каталог файл с фразами, с названием `new_phrases.json`
после чего запустите скрипт:
```sh
python add_intents.py
```

## Переменные окружения

Для запуска бота вам необходимо его зарегистрировать его у [Отца ботов](https://telegram.me/BotFather)

Для VK вам необходимо в настройках вашего сообщества получить ключ API во вкладке "Работа с API" 

Доступные переменные:
- `TELEGRAM_BOT_TOKEN` — Уникальный ключ для привязки к вашему боту
- `VK_GROUP_TOKEN` — Токен для доступа бота к сообщениям вашего сообщества в VK
- `PROJECT_ID` — ID вашего проекта на [Dialogflow](https://dialogflow.cloud.google.com)
- `USER_ID` - ID вышего профиля в Telegram для получения сообщений о ошибках бота (можно узнать [тут](https://t.me/getmyid_bot))

## Цели проекта

Код написан в учебных целях — для курса по Python и веб-разработке на сайте [Devman](https://dvmn.org).
