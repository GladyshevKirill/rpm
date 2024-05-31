"""Модуль обработки команды set_time"""
import re
from datetime import time

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext

from bot.states.set_time import SetTime
from bot.models import User
from bot.singleton import GlobalVars

router = Router()
TIME_PATTERN = r'^([0-9]|1[0-9]|2[0-3]):([0-5]\d)$'

@router.message(Command("set_time"))
async def set_time_handler(message: Message, state: FSMContext):
    """Обработка команды set_time"""
    await state.set_state(SetTime.time)
    await message.answer("Выберите время в формате чч:мм для рассылки праздников")


@router.message(F.text, SetTime.time)
async def set_time_by_notification_handler(message: Message, state: FSMContext):
    """Обработка введоного времени"""
    match = re.match(TIME_PATTERN, message.text)
    if not match:
        await message.answer("Не верный формат!")
        return
    hour = int(match.group(1))
    minute = int(match.group(2))
    new_time = time(hour=hour, minute=minute)
    user = User.get(tg_user=message.from_user.id)
    user.time = new_time
    user.save()
    GlobalVars.SEND_TIME = new_time

    await state.clear()
    

    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='🌍 Международные праздники', callback_data='11'),
            InlineKeyboardButton(text='🇷🇺 Праздники в России',callback_data='22')
        ],
        [
            InlineKeyboardButton(text='☦️ Церковные праздники',callback_data='33'),
            InlineKeyboardButton(text='🎂 Дни рождения знаменитостей',callback_data='44')
        ],
        [
            InlineKeyboardButton(text='🪶Памятные даты в истории',callback_data='55'),
            InlineKeyboardButton(text='🎁 Кто сегодня отмечает именины',callback_data='6')
        ]
    ])
    await message.answer("Время успешно записано!\n\nТеперь выберите категории, которые вас интересуют", reply_markup=inline_markup)

@router.message(SetTime.time)
async def set_other_by_notification_handler(message: Message):
    """Срабатывает когда пользователь отправляет не текст со временем"""
    await message.answer("Выберите время в формате чч:мм для рассылки праздников")
