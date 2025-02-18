import peewee
import requests
from bs4 import BeautifulSoup
from models import Games

def get_games(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features='html.parser')

    games = soup.find_all("div", class_="responsive_search_name_combined")
    for current_game in games:
        try:
            title = current_game.find("span", class_="title").text.strip()
            price = current_game.find("div", class_="discount_final_price").text.strip()
            if price == 'Free':
                new_game = Games(title=title, price=price, is_Free=1)
            else:
                new_game = Games(title=title, price=price, is_Free=0)
            new_game.save()
        except AttributeError:
            price = "Не найдено"
        except peewee.IntegrityError:
            pass


