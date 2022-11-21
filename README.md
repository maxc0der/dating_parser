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
Убедитесь, что с вашего аккаунта Вконтакте существует диалог с ботом Леонардо Дайвинчик, и последнее сообщение - анкета, доступная для оценки. 
Запустите main.py
