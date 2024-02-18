from random import randint

from environs import Env

import requests

env = Env()
env.read_env()
TOKEN = env('TOKEN')
URL = 'https://cloud-api.yandex.net/v1/disk/resources'
FOLDER_NAME = randint(0, 1000)
HEADERS = {'Authorization': TOKEN}
PARAMS = {'path': f'{FOLDER_NAME}'}


def create_folder():
    response = requests.put(URL, headers=HEADERS, params=PARAMS)
    return response.status_code


def check_if_folder_exists():
    response = requests.get(URL, headers=HEADERS, params=PARAMS)
    return response.json()['name'] == str(FOLDER_NAME)


if __name__ == '__main__':
    create_folder()
    check_if_folder_exists()
