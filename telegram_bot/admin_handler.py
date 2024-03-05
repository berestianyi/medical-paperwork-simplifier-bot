from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from config import admin_id, helsi_data
from core import sign_in, extract_appointment_code, fill_in_appointment_code
from telegram_bot.admin_kb import user_choice, def_choice

from database.orm import ORM

admin_router = Router()


class User(StatesGroup):
    user: dict = State()


@admin_router.message(CommandStart())
async def command_start(message: Message):
    if message.from_user.id == admin_id:
        await message.answer(f"Шалом, {message.from_user.first_name}\n"
                             f"З кого розпочинаємо?", reply_markup=user_choice)
    else:
        await message.answer(f'Цей бот зроблений тільки для одного користувача')


@admin_router.message((F.from_user.id == admin_id) & (F.text.startswith('Розпочинаємо')))
async def find_codes(message: Message, state: FSMContext):
    action = message.text.split(" з ")[1]
    await state.clear()

    if action == helsi_data['Г.Л.'].get('name'):
        user: dict = helsi_data['Г.Л.']
        await state.update_data(user=helsi_data['Г.Л.'])
    elif action == helsi_data['К.О.'].get('name'):
        user: dict = helsi_data['К.О.']
        await state.update_data(user=helsi_data['К.О.'])
    else:
        raise Exception

    await message.answer(f"Меню для користувача {user['name']}", reply_markup=def_choice)


@admin_router.callback_query((F.from_user.id == admin_id) & (F.data.startswith("choice_")))
async def user_menu(callback: CallbackQuery, state: FSMContext):
    action = callback.data.split("_")[1]
    user_list = await state.get_data()
    user = user_list.get('user')

    if action == 'search':
        sign_in.sign_in_helsi(user)
        extract_appointment_code.extraction_of_appointment_code_into_text(user)
        await callback.message.answer(f"Меню для користувача {user['name']}", reply_markup=def_choice)

    elif action == 'add':
        await callback.message.answer(f"Надсилайте коди")

    elif action == 'close':
        sign_in.sign_in_helsi(user)
        fill_in_appointment_code.filling_out_appointment_card(user)
        await callback.message.answer(f"Меню для користувача {user['name']}", reply_markup=def_choice)

    elif action == 'exit':
        await state.clear()
        await callback.message.answer(f"З кого розпочинаємо?", reply_markup=user_choice)


@admin_router.message((F.from_user.id == admin_id) & (F.text.regexp(r'\d{4}[-]\d{4}[-]\d{4}[-]\d{4}')))
async def add_more_codes(message: Message, state: FSMContext):
    user_list = await state.get_data()
    user = user_list['user']
    message_list = message.text.split('\n')
    for code in message_list:
        ORM.insert_data_unique_code(code=code, user=user['text_name'])
    await message.answer(f"Меню для користувача {user['name']}", reply_markup=def_choice)



