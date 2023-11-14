"""Файл, в котором будет происходить запуск бота и его найстрока
(считывание переменных окружения, импорт наших моудлей и т.п.)"""
import os
import rest_api
from flask import Flask, request, jsonify

app = Flask(__name__)

# SESSION_ID – id сессии, в которой должен участвовать бот
# BOT_URL – url для обратной коммуникации медиатора с ботом. Должен передаваться в запросе на регистрацию в сессии
# MEDIATOR_URL – base url, по которому бот может зарегистрироваться в сессии


if __name__ == "__main__":

    password = ""
    # id сессии, в которой должен участвовать бот
    SESSION_ID = os.environ['SESSION_ID']
    # URL для обратной коммуникации медиатора с ботом. Должен передаваться в запросе на регистрацию в сессии
    BOT_URL = os.environ['BOT_URL']
    bot_id = BOT_URL[0:str(BOT_URL).find(":")]
    # base url, по которому бот может зарегистрироваться в сессии
    MEDIATOR_URL = os.environ['MEDIATOR_URL']
    print(BOT_URL[0:str(BOT_URL).find(':')])
    print(BOT_URL[str(BOT_URL).find(':') + 1:])
    app.run(port=BOT_URL[str(BOT_URL).find(':') + 1:])
    
    url = f"/bot/turn"
    @app.route(url, methods=['POST'])
    def take_a_turn():
        data = request.json
        print(data)
        return 200
    print(BOT_URL[str(BOT_URL).find(':') + 1:])
    rest_api.register_bot(mediator_url=MEDIATOR_URL,
                          session_id=SESSION_ID,
                          bot_url=BOT_URL,
                          bot_id=bot_id,
                          password=password)


