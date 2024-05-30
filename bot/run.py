import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, BotCommand, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from rbk1 import *



bot = Bot(token='7086038652:AAEKbcrL_Mod-9KNUf2jZGNBE_ZYj7ti0jg') #завершить - ctrl + C
dp = Dispatcher()



@dp.message(Command("start"))
async def start_handler(msg: Message):
    hello = 'Привет! Я бот, который сообщит тебе, какой сегодня праздник! Давай знакомиться =) Что желаешь узнать?'
    await bot.set_my_commands([
        BotCommand(command='start', description='Запуск/перезапуск бота'),
        BotCommand(command='help', description='Помощь'),
        BotCommand(command='info_today', description='За что пьем?'),
    ])
    
    markup = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=hello)]])

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
    await msg.answer(text=hello, reply_markup=inline_markup)

@dp.callback_query(F.data == '1')
async def callback_query_handler(callback_query:CallbackQuery):
    await callback_query.message.answer(text = word_s)

@dp.callback_query(F.data == '2')
async def callback_query_handler(callback_query:CallbackQuery):
    await callback_query.message.answer(text = rus_s)

@dp.callback_query(F.data == '3')
async def callback_query_handler(callback_query:CallbackQuery):
    await callback_query.message.answer(text = church_s)

@dp.callback_query(F.data == '4')
async def callback_query_handler(callback_query:CallbackQuery):
    await callback_query.message.answer(text = birthday_s)

@dp.callback_query(F.data == '5')
async def callback_query_handler(callback_query:CallbackQuery):
    await callback_query.message.answer(text = history_s)


@dp.callback_query(F.data == '6')
async def callback_query_handler(callback_query:CallbackQuery):
    await callback_query.message.answer(text = imenins_s)

@dp.message(Command('help'))
async def cmd_help(message: Message):
    file = open('help.txt', 'r', encoding='utf-8')
    text = file.read()
    await message.answer(text) 

@dp.message(Command('info_today'))
async def cmd_help(message: Message):
    await message.answer(site) 

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
        