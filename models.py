from peewee import *
import pytz
from datetime import datetime
db = SqliteDatabase('users.db')
db_2 = SqliteDatabase('steam.db')

class User(Model):
    username = CharField(unique=True)
    first_name = CharField(null=True)
    last_name = CharField(null=True)
    date_register = DateField()
    is_Admin = BooleanField(default=0)

    class Meta:
        database = db


class Todo(Model):
    user = ForeignKeyField(User, related_name='to_do')
    name = CharField()
    time_create = DateTimeField(default=datetime.now(pytz.timezone('Europe/Moscow')))
    do = BooleanField(default=0)

    class Meta:
        database = db


class Games(Model):
    title = CharField(unique=True)
    price = FloatField()
    is_Free = BooleanField(default=0)
    class Meta:
        database = db_2


Games.create_table()
Todo.create_table()
User.create_table()