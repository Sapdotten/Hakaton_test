"""Файл для реализцаии обмена запросами с сервером медитором
(возможно поделим на два файла - для получения запрсов и для отправки)"""
import requests
import json
import os
from flask import Flask, request, jsonify



# MEDIATOR_URL = os.environ['MEDIATOR_URL']
# url = f"http://{MEDIATOR_URL}/bot/turn"
# url = f"/bot/turn"

# @app.route(url, methods=['POST'])
# def take_a_turn():
#     data = request.json
#     print(data)

# def register_bot_in_session(mediator_url: str, session_id: str, bot_url: str, bot_id: str, password: str):
#     """
#     Функция для регистрации бота в сессии
#     :param mediator_url: url сервера
#     :param session_id: UUID сессии
#     :param bot_url: id бота + его порт
#     :param bot_id: id бота
#     :param password: пароль бота
#     :return:
#     """
#     url = f"http://{mediator_url}/sessions/{session_id}/registration"
#     headers = {'Content-Type': 'application/json'}
#     bot_data = {
#         "bot_id": bot_id,
#         "password": password,
#         "bot_url": bot_url
#     }
#     response = requests.post(url, data=json.dumps(bot_data), headers=headers)
#     if response.status_code == 200:
#         print("Бот успешно зарегистрирован в сессии")
#         return response.json()
#     elif response.status_code == 400:
#         print("Некорректный запрос")
#     elif response.status_code == 404:
#         print("Не найдена игровая сессия с таким session_id")
#     else:
#         print(f"Необработанный статус кода: {response.status_code}")


# def register_bot(bot_id: str, bot_password: str):
#     url = f"http://localhost:8080/commands/{bot_id}"
#     headers = {'Content-Type': 'text/plain'}
#     bot_data = {
#         "bot-password": bot_password
#     }
#     response = requests.post(url, data=json.dumps(bot_data), headers=headers)
#     if response.status_code == 200:
#         print("Команда с ботом успешно зарегистрирован")
#         return response.json()
#     elif response.status_code == 400:
#         print("Некорректный запрос")
#     elif response.status_code == 404:
#         print("Не найдена команда с id этого бота")
#     else:
#         print(f"Необработанный статус кода: {response.status_code}")

# curl --location --request PUT 'http://localhost:8080/commands/1' \ --header 'Content-Type: text/plain' \ --data '123'

# def turn(mediator_url: str):
#     url = f"http://{mediator_url}/bot/turn"
#     headers = {'accept: application/json',
#                'Content-Type: application/json'}
#     bot_data = {
#         "game_field":
#     }
