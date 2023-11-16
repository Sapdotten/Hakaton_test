import os
import json
import requests
from flask import Flask, request, jsonify
from urllib.parse import urlparse
from game import Field

# в эту переменную потом запишется та фигура, за которую мы будем играть
figure = 0
# Инициализация Flask приложения
app = Flask(__name__)

BOT_URL = os.environ["BOT_URL"]
parsed_url = urlparse(BOT_URL)
host = parsed_url.hostname
port = parsed_url.port

SESSION_ID = os.environ['SESSION_ID']
MEDIATOR_URL = os.environ['MEDIATOR_URL']

BOT_ID = os.environ["BOT_ID"]
BOT_PASSWORD = os.environ["BOT_PASSWORD_DOCKERFILE"]


# Маршрут для обработки ходов медиатора
@app.route('/bot/turn', methods=['POST'])
def make_move():
    # Получение данных из запроса

    # вывод значений для проверки работоспособности кода
    # print("ДЕЛАЮ ХОД")
    make_move_data = request.get_json()
    # Ваш алгоритм для выбора хода
    game = Field(make_move_data["game_field"], figure)
    # print(make_move_data["game_field"])
    game_field = game.make_turn()

    move = {"game_field": game_field}

    response = move
    return jsonify(response), 200, {'Content-Type': 'application/json'}


# Ваш алгоритм для выбора лучшего хода
def make_best_move(board):
    index = board.find("_")
    # Выполнить замену первого символа "_"
    new_string = board[:index] + figure + board[index + 1:]
    return new_string


url = f'{MEDIATOR_URL}/sessions/{SESSION_ID}/registration'
# вывод значений для проверки работоспособности кода
# print(url)
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}
data1 = {
    "bot_id": BOT_ID,
    "password": BOT_PASSWORD,
    "bot_url": BOT_URL
}
data = json.dumps(data1)
# вывод значений для проверки работоспособности кода
# print(data)
res = requests.post(url, headers=headers, data=data)

# Проверка наличия содержимого в ответе
if res.status_code == 200:
    print(res)
    print("json.load(res.text).get('figure') = ", json.loads(res.text)["figure"])
    figure = json.loads(res.text)["figure"]

else:
    print(f"Error: {res.status_code}")

if __name__ == "__main__":
    # вывод значений для проверки работоспособности кода
    # print("я зашёл")
    # print(BOT_URL)
    # print(SESSION_ID)
    # print(MEDIATOR_URL)
    # print(BOT_ID)
    # print(BOT_PASSWORD)
    # print(host)
    # print(port)
    # app.run(host=f'0.0.0.0', port=port)
    app.run(host=f'{host}', port=port)
