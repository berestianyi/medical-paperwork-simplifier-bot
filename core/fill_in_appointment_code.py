from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from utils.core import button_status_validation, card_text_validation, card_status_validation
from utils.webdriver_set_up_settings import *
from config import uniqe_text
from database.orm import ORM


async def filling_out_appointment_card(helsi_person, msg):
    try:
        await msg.answer(f"Заповнення для {helsi_person['name']} розпочалося")

        appointment_codes_list = ORM.select_today_codes(user=helsi_person['text_name'])

        one_time_file_input = True
        index = 0

        for appointment_code in appointment_codes_list:

            print('-------------------------')
            index += 1

            print(f"{appointment_code}   {index}/{len(appointment_codes_list)}")
            await msg.answer(f"{appointment_code}   {index}/{len(appointment_codes_list)}")

            appointment = driver.find_elements(By.CLASS_NAME, 'tooltip-parent')
            appointment[5].click()
            time.sleep(3)

            # Вводимо направлення
            input_appointment = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'form-control'))
            )
            input_appointment.clear()
            input_appointment.send_keys(appointment_code)

            # input_appointment_btn = driver.find_element(By.CLASS_NAME, 'btn-info')
            input_appointment_btn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'btn-info'))
            )
            input_appointment_btn.click()

            # робимо пошук всіх потрібних блоків
            # request_list = driver.find_element(By.CLASS_NAME, 'ServiceRequestsList')
            request_list = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'ServiceRequestsList'))
            )

            carts_count = request_list.find_elements(By.CLASS_NAME, 'card')
            time.sleep(5)

            for i in range(len(carts_count)):
                print('-------------------------')
                # робимо пошук всіх потрібних блоків
                cards = driver.find_elements(By.CLASS_NAME, 'card')
                print(f"{i+1}/{len(carts_count)}")

                text = cards[i].text.split('\n')

                if card_text_validation(text[2]) and card_status_validation(status0=text[0], status1=text[1]):

                    # card_button = cards[i].find_elements(By.CLASS_NAME, "btn-info")[1]
                    card_button = WebDriverWait(cards[i], 10).until(
                        EC.presence_of_all_elements_located((By.CLASS_NAME, "btn-info"))
                    )
                    print(text[2])
                    await msg.answer(f"{i+1}/{len(carts_count)}   {text[2]}")

                    if button_status_validation(card_button[1].text):
                        time.sleep(12)
                        print(f'find text: {card_button[1].text}')
                        card_button[1].click()
                        time.sleep(8)

                        confirm_button_div = driver.find_elements(By.CLASS_NAME, 'actions')
                        confirm_button = confirm_button_div[0].find_element(By.CLASS_NAME, 'btn-info')

                        actions = ActionChains(driver)
                        actions.move_to_element(confirm_button).perform()
                        time.sleep(1)

                        confirm_button.click()
                        print(f'clicked button: {confirm_button.text}')
                        time.sleep(9)

                        health_place = driver.find_element(By.ID, 'locationId')
                        health_place.send_keys('філія №3')
                        time.sleep(2)
                        health_place.send_keys(Keys.ENTER)
                        print('нажано на філію')
                        time.sleep(3)

                        for conclusion_type in uniqe_text:
                            if text[2] == conclusion_type:
                                print('Found needed argument')
                                conclusion_fill = driver.find_element(By.ID, 'conclusion')
                                conclusion_fill.send_keys('Проведено.')
                                time.sleep(5)
                                print('wrote needed text')

                        success_button = driver.find_element(By.CLASS_NAME, 'btn-success')
                        success_button.click()
                        print('clicked on success button')
                        time.sleep(7)

                        if one_time_file_input:
                            select_key_file = driver.find_elements(By.ID, 'selectKeyFile')
                            select_key_file[1].send_keys(helsi_person['helsi_key'])
                            time.sleep(2)

                            accept_button = driver.find_elements(By.CLASS_NAME, 'storage-sign')
                            print('found sign button')
                            accept_button[2].click()
                            print('clicked on sign button')
                            time.sleep(5)

                            input_password = driver.find_elements(By.XPATH, "//input[@type='password']")
                            input_password[1].send_keys(helsi_person['helsi_key_password'])
                            time.sleep(2)

                            accept_button = driver.find_elements(By.CLASS_NAME, 'storage-sign')
                            print('found sign button')
                            accept_button[2].click()
                            print('clicked on sign button')
                            time.sleep(5)

                            one_time_file_input = False
                        else:

                            accept_button = driver.find_elements(By.CLASS_NAME, 'storage-sign')
                            print('found sign button')
                            accept_button[2].click()
                            print('clicked on sign button')
                            time.sleep(5)

                        appointment = driver.find_elements(By.CLASS_NAME, 'tooltip-parent')
                        appointment[5].click()
                        time.sleep(3)

                        # Вводимо направлення
                        input_appointment = driver.find_element(By.CLASS_NAME, 'form-control')
                        # input_appointment = WebDriverWait(driver, 10).until(
                        #     EC.presence_of_element_located((By.CLASS_NAME, 'form-control'))
                        # )

                        input_appointment.clear()
                        input_appointment.send_keys(appointment_code)
                        time.sleep(3)

                        input_appointment_btn = driver.find_element(By.CLASS_NAME, 'btn-info')
                        # input_appointment_btn = WebDriverWait(driver, 10).until(
                        #     EC.presence_of_element_located((By.CLASS_NAME, 'btn-info'))
                        # )
                        input_appointment_btn.click()
                        time.sleep(3)

        time.sleep(4)

    except Exception as ex:
        print(ex)
        await msg.answer(f"Виникла помилка \n\n {ex}")

    finally:
        driver.close()

        