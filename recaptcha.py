import asyncio
from python_rucaptcha.ImageCaptcha import ImageCaptcha, aioImageCaptcha

RUCAPTCHA_KEY = ""


def captcha_url(url):
    image_captcha = ImageCaptcha(rucaptcha_key=RUCAPTCHA_KEY)
    result = image_captcha.captcha_handler(captcha_link=url)
    return result['captchaSolve']


def captcha_file(path):
    image_captcha = ImageCaptcha(rucaptcha_key=RUCAPTCHA_KEY)
    result = image_captcha.captcha_handler(captcha_file=path)
    return result['captchaSolve']
