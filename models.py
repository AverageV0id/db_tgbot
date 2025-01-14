from peewee import *

db = SqliteDatabase('users.db')


class User(Model):
    username = CharField()
    date_register = DateField()
    is_Admin = BooleanField()

    class Meta:
        database = db


User.create_table()
