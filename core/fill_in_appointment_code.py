from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import os
import time

from webdriver_set_up_settings import *
from config import uniqe_text, appointment_codes_file


def filling_out_appointment_card(helsi_person):
    try:
        with open(appointment_codes_file, 'r') as f:
            appointment_codes = f.read()

        appointment_codes_list = appointment_codes.split('\n')

        one_time_file_input = True

        for appointment_code in appointment_codes_list:

            print('-------------------------')
            appointment = driver.find_elements(By.CLASS_NAME, 'tooltip-parent')
            appointment[5].click()
            time.sleep(3)

            # Вводимо направлення
            input_appointment = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'form-control'))
            )
            input_appointment.clear()
            input_appointment.send_keys(appointment_code)
            print(f'input: {appointment_code}')

            input_appointment_btn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'btn-info'))
            )
            input_appointment_btn.click()

            # прогрузка всієї сторінки
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 3000);")
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2)

            # робимо пошук всіх потрібних блоків
            request_list = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'ServiceRequestsList'))
            )

            carts_count = request_list.find_elements(By.CLASS_NAME, 'card')
            time.sleep(5)

            for i in range(len(carts_count)):

                print(f'card numbere {i}/{len(carts_count)}')

                # робимо пошук всіх потрібних блоків
                carts = driver.find_elements(By.CLASS_NAME, 'card')

                text = carts[i].text.split('\n')

                match = re.match(r"\d+-\d+\s([А-ЩЬЮЯҐЄІЇа-щьюяґєії'\s])+", text[2])
                match3 = re.match(r"^[5]{1}\d+-\d+\s([А-ЩЬЮЯҐЄІЇа-щьюяґєії'\s])+", text[2])

                if match and text[0] == 'Активне' and text[1] == 'Нове' and not match3:

                    cart_button = carts[i].find_elements(By.CLASS_NAME, "btn-info")[1]
                    print(text[2])

                    if cart_button.text == 'Заповнити процедуру' or cart_button.text == 'Заповнити звіт':
                        time.sleep(3)
                        print(f'find text: {cart_button.text}')
                        cart_button.click()
                        time.sleep(9)

                        confirm_button_div = driver.find_elements(By.CLASS_NAME, 'actions')
                        confirm_button = confirm_button_div[0].find_element(By.CLASS_NAME, 'btn-info')

                        actions = ActionChains(driver)
                        actions.move_to_element(confirm_button).perform()
                        time.sleep(1)

                        confirm_button.click()
                        print(f'clicked button: {confirm_button.text}')
                        time.sleep(10)

                        health_place = driver.find_element(By.ID, 'locationId')
                        health_place.send_keys('філія №3')
                        time.sleep(1)
                        health_place.send_keys(Keys.ENTER)
                        print('нажано на філію')
                        time.sleep(2)

                        for conclusion_type in uniqe_text:
                            if text[2] == conclusion_type:
                                print('Found needed argument')
                                conclusion_fill = driver.find_element(By.ID, 'conclusion')
                                conclusion_fill.send_keys('Проведено.')
                                time.sleep(3)
                                print('wrote "Проведено."')

                        success_button = driver.find_element(By.CLASS_NAME, 'btn-success')
                        success_button.click()
                        print('clicked on success card button')
                        time.sleep(10)

                        if one_time_file_input:
                            select_key_file = driver.find_elements(By.ID, 'selectKeyFile')
                            select_key_file[1].send_keys(helsi_person['helsi_key'])
                            time.sleep(2)

                            accept_button = driver.find_elements(By.CLASS_NAME, 'storage-sign')
                            accept_button[2].click()
                            print(f'clicked button {accept_button[2].text}')
                            time.sleep(5)

                            input_password = driver.find_elements(By.XPATH, "//input[@type='password']")
                            input_password[1].send_keys(helsi_person['helsi_key_password'])
                            time.sleep(2)

                            accept_button = driver.find_elements(By.CLASS_NAME, 'storage-sign')
                            accept_button[2].click()
                            print(f'clicked button: ПІДПИСАТИ')
                            time.sleep(8)

                            one_time_file_input = False
                        else:

                            accept_button = driver.find_elements(By.CLASS_NAME, 'storage-sign')
                            accept_button[2].click()
                            print(f'clicked button: ПІДПИСАТИ')
                            time.sleep(4)

                        appointment = driver.find_elements(By.CLASS_NAME, 'tooltip-parent')
                        appointment[5].click()
                        time.sleep(3)

                        # Вводимо направлення
                        input_appointment = driver.find_element(By.CLASS_NAME, 'form-control')
                        # input_appointment = WebDriverWait(driver, 10).until(
                        #     EC.presence_of_element_located((By.CLASS_NAME, 'form-control'))
                        # )
                        print("-------------------------")
                        input_appointment.clear()
                        input_appointment.send_keys(appointment_code)
                        print(f'input: {appointment_code}')
                        time.sleep(3)

                        input_appointment_btn = driver.find_element(By.CLASS_NAME, 'btn-info')
                        # input_appointment_btn = WebDriverWait(driver, 10).until(
                        #     EC.presence_of_element_located((By.CLASS_NAME, 'btn-info'))
                        # )
                        input_appointment_btn.click()
                        time.sleep(4)

        time.sleep(4)

        f.close()


        # -------------------------------- cookies ---------------------------------------
        # pickle.dump(driver.get_cookies(), open('my_cookies', 'wb'))
        # for cookie in pickle.load(open('my_cookies', 'rb')):
        #     driver.add_cookie(cookie)
        #
        # time.sleep(5)
        # driver.refresh()
        # time.sleep(5)

    except Exception as ex:
        print(ex)

    else:
        os.remove(appointment_codes_file)

        