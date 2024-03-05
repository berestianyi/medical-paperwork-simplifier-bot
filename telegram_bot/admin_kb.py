from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import helsi_data


user_choice = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=[
    [KeyboardButton(text=f"Розпочинаємо з {helsi_data['Г.Л.'].get('name')}")],
    [KeyboardButton(text=f"Розпочинаємо з {helsi_data['К.О.'].get('name')}")]
])


def_choice = InlineKeyboardMarkup(row_width=3, inline_keyboard=[
    [InlineKeyboardButton(
        text=f"Знайти направлення",
        callback_data=f"choice_search")],
    [InlineKeyboardButton(
        text=f"Ввести направлення",
        callback_data=f"choice_add")],
    [InlineKeyboardButton(
        text=f"Закривати направлення",
        callback_data=f"choice_close")],
    [InlineKeyboardButton(
        text=f"Змінити користувача",
        callback_data=f"choice_exit")]
])

