# _2. Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
# Выполнить запросы к нему, пройдя авторизацию.
# Ответ сервера записать в файл.

import requests
import json

URL = 'https://api.openweathermap.org/data/2.5/weather'
LAT = '33.44'
LON = '-94.04'
APPID = '7e4fe95a8e5126300e78aa2328db286f'
PARAMS = f'appid={APPID}'


def get_location(lat: str, lon: str) -> str:
    user_lat = input('Введите широту в формате ХХ.ХХ : ')
    user_lon = input('Введите долготу в формате ХХ.ХХ : ')
    lat = user_lat if user_lat else lat
    lon = user_lon if user_lon else lon
    return f'lat={lat}&lon={lon}'


def get_data() -> json:
    location = get_location(lat=LAT, lon=LON)
    url = f'{URL}?{location}&{PARAMS}'
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        print(url)
    return response.json()


def main():
    response = get_data()

    print('Получен результат')
    print(response)

    with open('lesson_1_2.json', 'w') as result:
        json.dump(response, result, indent=2)


if __name__ == '__main__':
    main()
