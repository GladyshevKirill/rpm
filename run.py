import asyncio

from config import TOKEN
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command
from aiogram.types import Message, BotCommand, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from bot.rbk1 import *

from handlers import include_routers
from models import User
from singleton import GlobalVars
from models import User
from datetime import time, timedelta, datetime



bot = Bot(token=TOKEN) #завершить - ctrl + C
dp = Dispatcher()
router = Router()



@dp.message(Command("start"))
async def start_handler(message: Message):
    hello = 'Привет! Я бот, который сообщит тебе, какой сегодня праздник! Давай знакомиться =)\n\n Введи /set_time, чтобы получать праздники каждый день)\n\n Что желаешь узнать?'
    await bot.set_my_commands([
        BotCommand(command='start', description='Запуск/перезапуск бота'),
        BotCommand(command='help', description='Помощь'),
        BotCommand(command='set_time', description='Установить время рассылки')
    ])

    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='🌍 Международные праздники', callback_data='1'),
            InlineKeyboardButton(text='🇷🇺 Праздники в России',callback_data='2')
        ],
        [
            InlineKeyboardButton(text='☦️ Церковные праздники',callback_data='3'),
            InlineKeyboardButton(text='🎂 Дни рождения знаменитостей',callback_data='4')
        ],
        [
            InlineKeyboardButton(text='🪶Памятные даты в истории',callback_data='5'),
            InlineKeyboardButton(text='🎁 Кто сегодня отмечает именины',callback_data='6')
        ]
    ])
    await message.answer(text=hello, reply_markup=inline_markup)

@dp.callback_query(F.data == '1')
async def callback_query_handler(callback_query:CallbackQuery):
    kb_back = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Назад', callback_data='back')]
    ])
    await callback_query.message.edit_text(text = word_s, reply_markup=kb_back)

@dp.callback_query(F.data == '2')
async def callback_query_handler(callback_query:CallbackQuery):
    kb_back = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Назад', callback_data='back')]
    ])
    await callback_query.message.edit_text(text = rus_s, reply_markup=kb_back)

@dp.callback_query(F.data == '3')
async def callback_query_handler(callback_query:CallbackQuery):
    kb_back = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Назад', callback_data='back')]
    ])
    await callback_query.message.edit_text(text = church_s, reply_markup=kb_back)

@dp.callback_query(F.data == '4')
async def callback_query_handler(callback_query:CallbackQuery):
    kb_back = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Назад', callback_data='back')]
    ])
    await callback_query.message.edit_text(text = birthday_s, reply_markup=kb_back)

@dp.callback_query(F.data == '5')
async def callback_query_handler(callback_query:CallbackQuery):
    kb_back = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Назад', callback_data='back')]
    ])
    await callback_query.message.edit_text(text = history_s, reply_markup=kb_back)


@dp.callback_query(F.data == '6')
async def callback_query_handler(callback_query:CallbackQuery):
    kb_back = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Назад', callback_data='back')]
    ])
    await callback_query.message.edit_text(text = imenins_s, reply_markup=kb_back)

@dp.callback_query(F.data == 'back')
async def callback_query_handler(callback_query: CallbackQuery):
    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='🌍 Международные праздники', callback_data='1'),
            InlineKeyboardButton(text='🇷🇺 Праздники в России',callback_data='2')
        ],
        [
            InlineKeyboardButton(text='☦️ Церковные праздники',callback_data='3'),
            InlineKeyboardButton(text='🎂 Дни рождения знаменитостей',callback_data='4')
        ],
        [
            InlineKeyboardButton(text='🪶Памятные даты в истории',callback_data='5'),
            InlineKeyboardButton(text='🎁 Кто сегодня отмечает именины',callback_data='6')
        ]
    ])
    await callback_query.message.edit_text(text='Привет! Я бот, который сообщит тебе, какой сегодня праздник! Давай знакомиться =)\n\nВведи /set_time, чтобы получать праздники каждый день)\n\nЧто желаешь узнать?', reply_markup=inline_markup)

@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(text='Команды, доступные в нашем боте:\n\n\
/start - запуск/перезапуск бота\n\
/help - гайд по всем командам бота\n\
/info_today - информация о праздниках сегодня\n\
/set_time - установка времени рассылки\n\n\
Если у вас возникли вопросы или бот не работает - писать @whypixi') 

@dp.message(Command('info_today'))
async def cmd_today(message: Message):
    await message.answer(site) 

async def get_time_notify():
    """Получить время ближайшего уведомления"""
    now = datetime.now()
    users = User.filter(User.time > now).order_by(User.time.asc())
    if users.count() > 0:
        return (users.first()).time

async def sending_messages():
    """Рассылка сообщений"""

    GlobalVars.SEND_TIME = await get_time_notify()
    while True:
        now_time = datetime.now().time()
        now_time = time(now_time.hour, now_time.minute)
        if GlobalVars.SEND_TIME and GlobalVars.SEND_TIME == now_time:
            # рассылка уведомлений всем пользователям
            for user in User.filter(time=GlobalVars.SEND_TIME):
                await bot.send_message(
                    chat_id=user.tg_user,
                    text='Ваше уведомление',
                )

            GlobalVars.SEND_TIME = await get_time_notify()

        now_time = (datetime.now() + timedelta(minutes=1))
        now_time = datetime(now_time.year, now_time.month, now_time.day,
                            now_time.hour, now_time.minute)
        seconds = (now_time - datetime.now()).seconds + 1
        await asyncio.sleep(seconds)

async def on_startup():
    """Обертка что бы запустить параллельный процесс"""
    asyncio.create_task(sending_messages())

async def main():
    dp.startup.register(on_startup)
    include_routers(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
        