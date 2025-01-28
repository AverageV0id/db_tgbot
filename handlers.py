import telebot
from datetime import date
import random
from models import *

from setting import *
from texts import get_users

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    try:
        if message.chat.username is None:
            new_user = User(username=str(message.chat.first_name) + str(message.chat.last_name),
                            first_name=str(message.chat.first_name), last_name=str(message.chat.last_name),
                            date_register=date.today(), is_Admin=True)
        elif message.chat.username == 'N0_th1n_g':
            new_user = User(username=message.chat.username, first_name=message.chat.first_name,
                            last_name=message.chat.last_name, date_register=date.today(), is_Admin=True)
        else:
            new_user = User(username=message.chat.username, first_name=message.chat.first_name,
                            last_name=message.chat.last_name, date_register=date.today(), is_Admin=False)
        new_user.save()
        bot.send_message(message.chat.id, f"Пользователь зарегестрирован\n ")
    except Exception as e:
        if type(e) == IntegrityError:
            bot.send_message(message.chat.id, f"Вы уже зарегистрированны\n ")
        else:
            bot.send_message(message.chat.id, f"Возникла ошибка: {e}\n ")


@bot.message_handler(commands=['search_db'])
def search_db(message):

        text = message.text[9::]
        admin = User.select().where((User.username == message.chat.username) | (
                    User.username == str(message.chat.first_name) + str(message.chat.last_name))).get()
        if admin.is_Admin == 1:
            bot.send_message(message.chat.id,
                                 f'Все пользователи: {get_users()}',
                                 parse_mode='Markdown')

            s_user =  User.select().where(User.username == text).get()
            bot.send_message(message.chat.id, f'Найден: {s_user.username}', parse_mode='Markdown')

        else:
            bot.send_message(message.chat.id, 'Вы не являетесь администратором')

        bot.send_message(message.chat.id, f'Ошибка: {e}')
