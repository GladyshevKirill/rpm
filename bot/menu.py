from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

key_main = KeyboardButton('⬅️ Главное меню')

#--------Menu
key_s_word = KeyboardButton('🌍 Международные праздники')
key_s_rus = KeyboardButton(' 🇷🇺 Праздники в России')
key_s_vera = KeyboardButton('☦️ Церковные праздники')
key_s_birthday = KeyboardButton('🎂 Дни рождения знаменитостей')
key_s_history = KeyboardButton('🪶Памятные даты в истории')
key_s_imenin = KeyboardButton('🎁 Кто сегодня отмечает именины')
key_next = KeyboardButton('Другое ➡️')
mainMenu = ReplyKeyboardMarkup(resize_keyboard= True).add(key_s_word, key_s_birthday, key_s_history, key_s_rus, key_s_imenin, key_s_vera, key_next)

#-----OtherMenu

key_start = KeyboardButton('Запуск/перезапуск бота')
key_help = KeyboardButton('Помощь')
othMenu = ReplyKeyboardMarkup(resize_keyboard= True).add(key_start, key_help, key_main)