from models import User
from models import Todo
commands = ('Список комманд(/help, /info, /commands):\n '
            '/start - запустить бота \n '
            '/get_message - отправляет информацию о сообщении \n '
            '/calculate - выводит ответ примера \n'
            '/echo - вывести своё же сообщение(работает если в простом сообщении сказать "эхо" \n'
            '/bar - вывести картинку стобчатую диаграмму (пример /bar 1 2 3, 1 2 3)) \n'
            '/graph - вывести картинку нескольких точек (пример /graph 10, 10, 1, y=x*x))'
            '/graphs - вывести картинку нескольких функций (пример /graphs -10 10 1 y=x*x, -10 10 1 y=-x*x))')
invalid_message = 'Я не понимаю твоё сообщение, используйте /help(/commands, /info) для просмотра списка комманд'


def get_users():
    text_users = ''
    for user in User:
        text_users += f'{user.username} | {user.first_name} | {user.last_name} |{user.date_register} | {user.is_Admin} \n'
    return str(text_users)

def get_todos(filter):
    text_todos = ''
    for todo in filter:
        text_todos += f'{todo.name} | {todo.do}  \n'
    return str(text_todos)