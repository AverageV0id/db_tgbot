from models import *

for user in User.select():
    print('Удалён: ', user.username)
    user.delete_instance()
