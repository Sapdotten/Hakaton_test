"""Файл, в котором будет происходить запуск бота и его найстрока
(считывание переменных окружения, импорт наших моудлей и т.п.)"""
import os
import rest_api

# SESSION_ID – id сессии, в которой должен участвовать бот
# BOT_URL – url для обратной коммуникации медиатора с ботом. Должен передаваться в запросе на регистрацию в сессии
# MEDIATOR_URL – base url, по которому бот может зарегистрироваться в сессии


if __name__ == "__main__":
    bot_id = ""
    password = ""
    # id сессии, в которой должен участвовать бот
    SESSION_ID = os.environ.get('SESSION_ID')
    print(SESSION_ID)
    # URL для обратной коммуникации медиатора с ботом. Должен передаваться в запросе на регистрацию в сессии
    BOT_URL = os.environ.get('BOT_URL')
    # base url, по которому бот может зарегистрироваться в сессии
    MEDIATOR_URL = os.environ.get('MEDIATOR_URL')

    rest_api.register_bot(mediator_url=MEDIATOR_URL,
                          session_id=SESSION_ID,
                          bot_url=BOT_URL,
                          bot_id=bot_id,
                          password=password)

