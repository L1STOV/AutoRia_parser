from bs4 import BeautifulSoup
import requests
from prettytable import PrettyTable


def parse():
    URL = "https://auto.ria.com/legkovie/bmw/325/"
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/83.0.4103.106 Safari/537.36 '
    }

    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('div', class_='content')

    cars = []

    for item in items:
        cars.append({
            'title': item.find('a', class_='address').get_text(strip = True),
            'price': item.find('span', class_ ='bold green size22').get_text(strip = True),
            'location': item.find('li', class_='item-char view-location').get_text(strip = True),
            'runtime': item.find('li', class_='item-char').get_text(strip = True)
        })

    table = PrettyTable()
    table.field_names = ['Название авто', "Цена", "Локация", "Пробег"]
    for car in cars:
        table.add_row([car['title'], car['price'], car['location'], car['runtime']])
    print(table)


parse()
