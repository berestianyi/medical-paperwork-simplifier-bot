from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from utils.webdriver_set_up_settings import *


async def sign_in_helsi(helsi_person, msg):
    try:
        driver.get('https://id.helsi.pro/account/login')
        time.sleep(2)

        await msg.answer(f"Вхід для {helsi_person['name']} розпочався")

        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'email'))
        )
        email_input.clear()
        email_input.send_keys(helsi_person['email'])
        print("Email is entered")
        await msg.answer(f"Email введено")

        time.sleep(1)

        password_input = WebDriverWait(driver,  10).until(
            EC.presence_of_element_located((By.ID, 'usercreds'))
        )
        password_input.clear()
        password_input.send_keys(helsi_person['password'])
        print("Password is entered")
        await msg.answer(f"Пароль введено")

        time.sleep(1)

        log_in_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@type="submit"]'))
        )
        log_in_button.click()
        print("Log in success")
        await msg.answer(f"Вхід успішний")

        time.sleep(7)

    except Exception as ex:
        print(ex)
        await msg.answer(f"Виникла помилка \n\n {ex}")
