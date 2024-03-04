from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time

from webdriver_set_up_settings import *
from config import appointment_codes_file
from database.orm import ORM


def extraction_of_appointment_code_into_text(user):

    try:
        # file = open(appointment_codes_file, 'a')
        # ------------------------------------------
        homepage_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'timeline-home-page-um'))
        )
        homepage_button.click()
        print("Homepage is clicked")

        # past_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, 'past'))
        # )
        # past_button.click()
        # print("Past is clicked")

        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 2000);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)

        all_appointment_cards = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'timeline-item-right'))
        )
        print(len(all_appointment_cards))

        for i in range(len(all_appointment_cards)):

            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 2000);")
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2)

            finished_appointment_cards = WebDriverWait(driver, 5).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'timeline-item-content-state-finished'))
            )
            print("finished appointment card is found")

            if finished_appointment_cards:

                appointment_card_button = WebDriverWait(finished_appointment_cards[i], 5).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, 'btn'))
                )
                print("finished appointment card button is found")

                if appointment_card_button[2].text == 'Переглянути прийом':
                    time.sleep(1)
                    appointment_card_button[2].click()
                else:
                    raise Exception("there is no button called 'Переглянути прийом'")

                e_appointment_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.ID, 'link_service-records'))
                )
                e_appointment_button.click()

                time.sleep(1)
                e_appointment_card_code = driver.find_elements(By.CLASS_NAME, 'ServiceRecordListItem_form__item__w7Vhw')
                time.sleep(1)

                if e_appointment_card_code and re.match(r"\d+-\d+-\d+-\d+", e_appointment_card_code[0].text):
                    print(e_appointment_card_code[0].text)

                    ORM.insert_data_unique_code(user=user['text_name'], code=e_appointment_card_code[0].text)
                    # file.write(e_appointment_card_code[0].text + "\n")

            driver.back()
            driver.back()

        time.sleep(5)
        # file.close()

    except Exception as ex:
        print(ex)
