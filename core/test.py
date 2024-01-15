# import re
# from config import uniqe_text
#
#
# text = "96027-00 Спостереження за прийомом призначених/самостійно обраних лікарських засобів"
#
# match2 = re.match(r"\d+-\d+\s([А-ЩЬЮЯҐЄІЇа-щьюяґєії'\s])+", text)
#
# if match2:
#     print(match2)
#
# for i in uniqe_text:
#     if text == i:
#         print("okey")
#
#
# with open('../appointment_codes', 'r') as f:
#     appointment_codes = f.read()
#
# appointment_codes_list = appointment_codes.split('\n')
#
# print(appointment_codes_list)