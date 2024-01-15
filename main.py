from core import extract_appointment_code, fill_in_appointment_code, sign_in
from webdriver_set_up_settings import *
from config import helsi_data, appointment_codes_file
import os

# варіанти такі 'Г.Л.' and 'К.О.'
helsi_person = helsi_data['Г.Л.']


def main():
    try:
        if os.path.exists(appointment_codes_file):
            os.remove(appointment_codes_file)

        sign_in.sign_in_helsi(helsi_person)

        extract_appointment_code.extraction_of_appointment_code_into_text()

        fill_in_appointment_code.filling_out_appointment_card(helsi_person)

    except Exception as ex:
        print(ex)
    finally:
        print('mission complete, boss')
        driver.close()
        driver.quit()


if __name__ == "__main__":
    main()