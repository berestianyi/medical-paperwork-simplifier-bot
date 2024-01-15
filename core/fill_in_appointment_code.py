from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
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

            appointment = driver.find_elements(By.CLASS_NAME, 'tooltip-parent')
            appointment[5].click()
            time.sleep(3)

            # Вводимо направлення
            # input_appointment = driver.find_element(By.CLASS_NAME, 'form-control')
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
            # carts_count = WebDriverWait(request_list, 10).until(
            #     EC.presence_of_all_elements_located((By.CLASS_NAME, 'card'))
            # )
            # print(carts_count[5].text)
            # print(carts[0].text)

            for i in range(len(carts_count)):
                # робимо пошук всіх потрібних блоків
                carts = driver.find_elements(By.CLASS_NAME, 'card')
                print(carts[0].text)

                text = carts[i].text.split('\n')
                print(text[1])

                match = re.match(r"\d+-\d+\s([А-ЩЬЮЯҐЄІЇа-щьюяґєії'\s])+", text[1])
                match2 = 'АктивнеНове'
                match3 = '58500-00 Рентгенографія грудної клітки'

                if match and text[0] == match2 and text[0] != match3:
                    cart = carts[i].find_elements(By.CLASS_NAME, "btn-info")[1]
                    time.sleep(5)
                    print(f'find text: {cart.text}')
                    cart.click()
                    print('clicked on this text')
                    time.sleep(6)

                    confirm_button_div = driver.find_elements(By.CLASS_NAME, 'actions')
                    confirm_button = confirm_button_div[0].find_element(By.CLASS_NAME, 'btn-info')
                    confirm_button.click()
                    print('нажано на кнопку підтвердити')
                    time.sleep(7)

                    health_place = driver.find_element(By.ID, 'locationId')
                    health_place.send_keys('філія №3')
                    time.sleep(2)
                    health_place.send_keys(Keys.ENTER)
                    print('нажано на філію')
                    time.sleep(5)

                    for conclusion_type in uniqe_text:
                        if text[1] == conclusion_type:
                            print('Found needed argument')
                            conclusion_fill = driver.find_element(By.ID, 'conclusion')
                            conclusion_fill.send_keys('Проведено.')
                            time.sleep(5)
                            print('wrote needed text')

                    success_button = driver.find_element(By.CLASS_NAME, 'btn-success')
                    print('found success button')
                    success_button.click()
                    print('clicked on success button')
                    time.sleep(7)

                    if one_time_file_input:
                        select_key_file = driver.find_elements(By.ID, 'selectKeyFile')
                        select_key_file[1].send_keys(helsi_person['helsi_key'])
                        time.sleep(2)

                        accept_button = driver.find_elements(By.CLASS_NAME, 'storage-sign')[2]
                        print('found sign button')
                        accept_button.click()
                        print('clicked on sign button')
                        time.sleep(5)

                        input_password = driver.find_elements(By.XPATH, "//input[@type='password']")
                        input_password[1].send_keys(helsi_person['helsi_key_password'])
                        time.sleep(2)

                        accept_button = driver.find_elements(By.CLASS_NAME, 'storage-sign')[2]
                        print('found sign button')
                        accept_button.click()
                        print('clicked on sign button')
                        time.sleep(5)

                        one_time_file_input = False
                    else:

                        accept_button = driver.find_elements(By.CLASS_NAME, 'storage-sign')[2]
                        print('found sign button')
                        accept_button.click()
                        print('clicked on sign button')
                        time.sleep(5)

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

        