from URLs import *
from data import *
import requests
import allure
import json


@allure.step('Создаем заказ через апи')
def create_order():

    payload = {
        'email': user_data[0],
        'password': user_data[1]
    }

    api_token = requests.post(URLS.api_login_url, data=payload).json()["accessToken"]

    headers = {
        'Content-Type': 'application/json',
        'authorization': api_token
    }

    payload = {
        'ingredients': '61c0c5a71d1f82001bdaaa6d'
    }

    response = requests.post(URLS.api_orders_url, data=json.dumps(payload), headers=headers)
    return response.json()['order']['number']