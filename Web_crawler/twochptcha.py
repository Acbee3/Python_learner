# https://github.com/2captcha/2captcha-python

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

config = {
            'apiKey':           'b1d034911826362731b84edb0bf4bb60',
            'defaultTimeout':    60,
            'recaptchaTimeout':  60,
        }
solver = TwoCaptcha(**config)

def image_to_string():
    try:
        result = solver.normal('D:\Code\Python\Web_crawler\\a.jpg')

    except Exception as e:
        sys.exit(e)

    else:
        sys.exit('solved: ' + str(result))
    finally:
        return result.get('code')