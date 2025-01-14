import telebot
from datetime import date
from models import *

from setting import *

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.username == 'N0_th1n_g':
        new_user = User(username=message.chat.username, date_register=date.today(), is_Admin=True)
    else:
        new_user = User(username=message.chat.username, date_register=date.today(), is_Admin=False)
    new_user.save()
    bot.send_message(message.chat.id, f"Пользователь зарегестрирован\n ")

@bot.message_handler(commands=['search_db'])
def search_db(message):
    text = message[9::]
    for user in User.select():
        bot.send_message(message.chat.id, user.username, user.date_register)

    bot.send_message(message.chat.id, '\n' * 2)

    for user in User.select().where(User.username == text):
        bot.send_message(message.chat.id, user.username)
        user.username = '💪'
        user.save()
