import time
from recaptcha import *
import requests
import json
import random


def create_session(proxy=None,
                   useragent='VKAndroidApp/8.5-14622 (Android 7.1.2; SDK 25; armeabi-v7a; samsung SM-N975F; zh; 1600x900)'):
    session = requests.Session()
    if proxy is not None:
        session.proxies = {'https': 'http://' + proxy, 'http': 'http://' + proxy}
    session.headers['User-agent'] = useragent
    session.headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=utf-8'
    session.headers['X-Quic'] = '1'
    return session


def resolve_captcha(url):
    print('Waiting captcha...')
    key = captcha_url(url)
    return key


def get_messages(session, params, user_id):
    params2 = {
        'user_id': user_id,
    }
    x = json.loads(session.post('https://api.vk.com/method/messages.getHistory', data=params | params2).text)
    message = x['response']['items'][0]
    text = message['text']
    name = text.split(',')[0]
    age = text.split(',')[1].strip()
    caption = text[text.find(',', text.find(',', text.find(',')+1)+1)+1:]
    photo = message['attachments'][0]['photo']['sizes'][0]['url']
    return {'name': name, 'age': age, 'caption': caption, 'photo': photo}


def send_answer(session, params, user_id, captcha_sid='', captcha_key=''):
    params2 = {
        'user_id': user_id,
        'message': '👎',
        'random_id': random.randint(0, 99999999),
        'payload': 3,
        'captcha_sid': captcha_sid,
        'captcha_key': captcha_key,
    }
    response = session.post('https://api.vk.com/method/messages.send', data=params | params2).text
    if 'need_captcha' in response:
        answer = json.loads(response)
        return send_answer(session, params, user_id,
                           captcha_sid=answer['captcha_sid'],
                           captcha_key=resolve_captcha(answer['captcha_img'].replace('\\', '')))
    x = json.loads(response)
    print(x)


def get_api_token(session, login='', password='', captcha_sid='', captcha_key=''):
    response = session.get(
        'https://api.vk.com/oauth/token',
        params={
            'grant_type': 'password',
            'client_id': 2274003,
            'scope': 'all,offline',
            'client_secret': 'hHbZxrka2uZ6jB1inYsH',
            'username': login,
            'password': password,
            'captcha_sid': captcha_sid,
            'captcha_key': captcha_key,
            'v': '5.196'
        }
    )
    answer = response.text
    if 'need_captcha' in answer:
        answer = json.loads(answer)
        return get_api_token(session, login, password,
                             captcha_sid=answer['captcha_sid'],
                             captcha_key=resolve_captcha(answer['captcha_img'].replace('\\', '')))

    if 'access_token' in json.loads(answer):
        return json.loads(answer)['access_token']
    else:
        print(answer)
        return False

