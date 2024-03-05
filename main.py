import asyncio
import logging
import sys

from core import extract_appointment_code, fill_in_appointment_code, sign_in
from utils.bot import dp, bot
from utils.webdriver_set_up_settings import *
from config import helsi_data
from telegram_bot import admin_router


async def main() -> None:

    dp.include_router(
        admin_router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    loop.run_forever()















































# варіанти такі 'Г.Л.' and 'К.О.'
# helsi_person = helsi_data['К.О.']


# def main():
#     # if os.path.exists(appointment_codes_file):
#     #
#     #     sign_in.sign_in_helsi(helsi_person)
#     #     fill_in_appointment_code.filling_out_appointment_card(helsi_person)
#     #
#     # else:
#     #     sign_in.sign_in_helsi(helsi_person)
#     #     extract_appointment_code.extraction_of_appointment_code_into_text(helsi_person)
#     #     fill_in_appointment_code.filling_out_appointment_card(helsi_person)
#
#     sign_in.sign_in_helsi(helsi_person)
#     extract_appointment_code.extraction_of_appointment_code_into_text(helsi_person)
#     fill_in_appointment_code.filling_out_appointment_card(helsi_person)
#
#     print('mission complete, boss')
#     driver.close()
#     driver.quit()
#
#
# if __name__ == "__main__":
#     main()

# name1 = 'g'
# name2 = 'k'
#
# code1 = '4796-1337-8088-2364'
# code2 = '9328-4171-5498-6844'
# code3 = '4603-3832-2180-4476'
# code4 = '4003-3832-2180-3230'
#
# from database.orm import ORM
#
# # ORM.create_table()
#
# ORM.insert_data_unique_code(user=name1, code=code1)
# ORM.insert_data_unique_code(user=name2, code=code2)
# ORM.insert_data_unique_code(user=name1, code=code2)
# ORM.insert_data_unique_code(user=name2, code=code4)
# ORM.insert_data_unique_code(user=name1, code=code3)
#
# print(ORM.select_today_codes(user=name1))
# print('----------------------------------')
# print(ORM.select_today_codes(user=name2))
