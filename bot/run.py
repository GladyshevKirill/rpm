import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


bot = Bot(token='7086038652:AAEKbcrL_Mod-9KNUf2jZGNBE_ZYj7ti0jg') #завершить - ctrl + C
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        'Привет! \n Я бот, который сообщит тебе, какие сегодня праздники отмечаются в стране и в мире!'
        )

@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('file') 

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
        