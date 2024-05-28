import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from rbk1 import site


bot = Bot(token='7086038652:AAEKbcrL_Mod-9KNUf2jZGNBE_ZYj7ti0jg') #завершить - ctrl + C
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):

    await message.answer(
        'Привет!'

'Я бот, который сообщит тебе, какой сегодня праздник!'

'Давай знакомиться =) Что желаешь узнать?'
    )

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
        