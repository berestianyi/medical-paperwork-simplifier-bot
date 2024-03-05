import re

from config import appointment_codes_file
from utils.webdriver_set_up_settings import driver


def card_text_validation(card_text):
    if re.match(r"^[5]{1}\d+-\d+\s([А-ЩЬЮЯҐЄІЇа-щьюяґєії'\s])+", card_text):
        return False
    elif card_text == 'B33006 Аналіз; ВІЛ':
        return True
    elif re.match(r"\d+-\d+\s([А-ЩЬЮЯҐЄІЇа-щьюяґєії'\s])+", card_text):
        return True


def card_status_validation(status0, status1):
    if status0 == 'Активне' and status1 == 'Нове':
        return True
    else:
        return False


def button_status_validation(status):
    if status == 'Заповнити процедуру' or status == 'Заповнити звіт':
        return True
    else:
        return False
