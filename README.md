# Установка

Загрузите репозиторий

```sh
git clone https://github.com/maxc0der/dating_parser
```

Установите требуемые библиотеки
```sh
pip install -r requirements.txt
```

В файл main.py укажите логин и пароль от аккаунта Вконтакте
```sh
token = get_api_token(session, login='LOGIN', password='PASSWORD')
```
В файл recaptcha.py укажите API ключ от https://rucaptcha.com/ (не обязтельно)
```sh
RUCAPTCHA_KEY = "PUT_KEY_HERE"
```
Создайте анкету в боте Леонардо Дайвинчик https://vk.com/dayvinchik

Перейдите к этапу просмотра анкет

Убедитесь, что последнее сообщение - анкета, доступная для оценки. 

Запустите main.py
