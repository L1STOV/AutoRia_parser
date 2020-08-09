from bs4 import BeautifulSoup
import requests
from car import Car
import time

while True:
    url = "https://auto.ria.com/legkovie/bmw/325/?page="

    count = 0
    list_of_parsed_cars = []


    def parse_cars(items):
        local_list_of_parsed_cars = []
        for item in items:
            car_object = Car()
            a_element = item.find('div', class_='content').find('a')
            span_element = item.find('span', class_='bold green size22')
            i_element = item.find('li', class_='item-char')
            car_object.url = a_element['href']
            car_object.title = a_element['title']
            car_object.price = span_element.get_text(strip=True)
            car_object.runtime = i_element.get_text(strip=True)
            local_list_of_parsed_cars.append(car_object)
        return local_list_of_parsed_cars


    while True:
        file = open("File.txt", "w", encoding="utf-8")
        print('Parsing ' + str(count) + ' page')
        response = requests.request("GET", url + str(count))
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('section', class_="ticket-item")
        parsed_cars = parse_cars(items)
        if len(parsed_cars) == 0:
            break
        for car in parsed_cars:
            list_of_parsed_cars.append(car)
        count += 1

    for car in list_of_parsed_cars:
        print(car.url)
        print(car.title)
        print(car.price + " $")
        print(car.runtime)
        print('\n')
        file.write(car.url + '\n')
    file.close()

    print('Parsing finished! ')
    print('Found ' + str(len(list_of_parsed_cars)) + ' cars')

    time.sleep(300)
