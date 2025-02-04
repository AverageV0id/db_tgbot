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
    try:
        text = message.text[10::]
        admin = User.select().where((User.username == message.chat.username) | (
                User.username == str(message.chat.first_name) + str(message.chat.last_name))).get()
        if admin.is_Admin == 1:
            if text == '' or text == ' ':
                bot.send_message(message.chat.id,
                                 f'Все пользователи: *{get_users()}*',
                                 parse_mode='Markdown')

            else:
                s_user = User.get(User.username == text)
                bot.send_message(message.chat.id, f'Найден: *{s_user.username}*',
                                 parse_mode='Markdown')

        else:
            bot.send_message(message.chat.id, 'Вы не являетесь администратором')


    except User.DoesNotExist:
        bot.send_message(message.chat.id, f'Пользователь не найден')
    except Exception as e:
        bot.send_message(message.chat.id, f'Произошла ошибка: {e}')


@bot.message_handler(commands=['give_admin'])
def give_admin(message):
    try:
        admin = User.select().where((User.username == message.chat.username) | (
                User.username == str(message.chat.first_name) + str(message.chat.last_name))).get()

        if admin.is_Admin == 1:
            bot.send_message(message.chat.id, 'Верификация Пройдена')
            text = message.text[11::].strip

            user = User.select().where((User.username == text)).get()

            if not user.is_Admin:
                bot.send_message(message.chat.id, f'*{user.username} теперь  Админ*')
                user.is_Admin = 1
                user.save()
            else:
                bot.send_message(message.chat.id, f"*{user.username} является Админом*")
        else:
            bot.send_message(message.chat.id, 'Вы не являетесь Админом')
    except User.DoesNotExist:
        bot.send_message(message.chat.id, f'Пользователь не найден')
    except Exception as e:
        bot.send_message(message.chat.id, f'Произошла ошибка: {e}')


@bot.message_handler(commands=['set_do'])
def set_do(message):
    text = message.text[7::]
    user = User.select().where((User.username == message.chat.username) | (
                User.username == str(message.chat.first_name) + str(message.chat.last_name))).get()
    new_todo = Todo(user=user, name=text)
    new_todo.save()
    bot.send_message(message.chat.id, f'Создано Дело: *{new_todo.name}*')

@bot.message_handler(commands=['todo_list'])
def todo_list(message):
    text = message.text[10::]
    todo_list = Todo.select().where(Todo.user == message.chat.username | (
                Todo.user == str(message.chat.first_name) + str(message.chat.last_name)))
    for todo in todo_list:
        bot.send_message(message.chat.id, f'Создано Дело: *{todo.name, todo.do}*')