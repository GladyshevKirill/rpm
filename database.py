import sqlite3

# Подключение к базе данных (или создание новой, если она не существует)
conn = sqlite3.connect('my_database.db')

# Создание курсора для работы с базой данных
cursor = conn.cursor()

# Создание таблицы с тремя колонками: id, name, age
cursor.execute('''CREATE TABLE IF NOT EXISTS день
                (id TEXT,
                name TEXT NOT NULL,
                age TEXT)''')

# Сохранение изменений в базе данных
conn.commit()

# Закрытие соединения с базой данных
conn.close()

print("База данных с тремя колонками успешно создана.")