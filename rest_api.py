"""Файл для реализцаии обмена запросами с сервером медитором
(возможно поделим на два файла - для получения запрсов и для отправки)"""
import requests
import json


def register_bot_in_session(mediator_url: str, session_id: str, bot_url: str, bot_id: str, password: str):
    url = f"http://{mediator_url}/sessions/{session_id}/registration"
    headers = {'Content-Type': 'application/json'}
    bot_data = {
        "bot_id": bot_id,
        "password": password,
        "bot_url": bot_url
    }
    response = requests.post(url, data=json.dumps(bot_data), headers=headers)
    if response.status_code == 200:
        print("Бот успешно зарегистрирован в сессии")
        return response.json()
    elif response.status_code == 400:
        print("Некорректный запрос")
    elif response.status_code == 404:
        print("Не найдена игровая сессия с таким session_id")
    else:
        print(f"Необработанный статус кода: {response.status_code}")


def bot_turn(mediator_url: str, game_field: str):
    url = f"http://{mediator_url}/bot/turn"
    headers = {'Content-Type': 'application/json'}
    game_field_data = {
        "game_field": game_field
    }
    response = requests.post(url, data=json.dumps(game_field_data), headers=headers)
    if response.status_code == 200:
        print("Бот успешно сходил")
        return response.json()
    else:
        print(f"Необработанный статус кода: {response.status_code}")

