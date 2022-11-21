import time
from recaptcha import *
import requests
import json
import os
import random
from vk_worker import *
import sql

session = create_session()
token = get_api_token(session, login='', password='')

if not os.path.exists('photo'):
    os.makedirs('photo')

if not os.path.exists('base.db'):
    sql.init()

params = {
    'lang': 'ru',
    'access_token': token,
    'v': '5.131'
}

while True:
    x = get_messages(session, params, '-91050183')
    response = requests.get(x['photo'])
    file_name = 'photo/' + str(random.randint(100000000, 999999999)) + '.jpg'
    with open(file_name, 'wb') as f:
        f.write(response.content)
    print(x)
    sql.store(x['name'], x['age'], x['caption'], x['photo'], file_name)
    send_answer(session, params, '-91050183')
    time.sleep(3)

