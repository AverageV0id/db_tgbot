from peewee import *

db = SqliteDatabase('users.db')


class User(Model):
    username = CharField(unique=True)
    first_name = CharField(null=True)
    last_name = CharField(null=True)
    date_register = DateField()
    is_Admin = BooleanField(default=0)

    class Meta:
        database = db


User.create_table()
