import peewee

# Определение модели данных
db = peewee.SqliteDatabase('database.db')

class EventModel(peewee.Model):
    date = peewee.DateField()
    event = peewee.CharField()

    class Meta:
        database = db

# Создание таблицы в базе данных
db.connect()
db.create_tables([EventModel])

# Заполнение таблицы данными из файла
with open('holiday.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        date, event = line.strip().split('-')
        EventModel.create(date=date, event=event)

db.close()