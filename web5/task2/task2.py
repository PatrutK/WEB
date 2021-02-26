import sys
from io import BytesIO
# Этот класс поможет нам сделать картинку из потока байт

import requests
from PIL import Image

toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}


def get_coordinates(toponym):

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        # обработка ошибочной ситуации
        pass

    # Преобразуем ответ в json-объект
    json_response = response.json()
    # Получаем первый топоним из ответа геокодера.
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    # Долгота и широта:
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    return (toponym_longitude, toponym_lattitude)


map_api_server = "http://static-maps.yandex.ru/1.x/"


def show_map(ll_spn, display_type):
    delta = "0.005"
    # Собираем параметры для запроса к StaticMapsAPI:
    map_params = {
        "ll": ",".join(list(get_coordinates(toponym_to_find))),
        "spn": ",".join([delta, delta]),
        "l": display_type
    }

    response = requests.get(map_api_server, params=map_params)

    Image.open(BytesIO(
        response.content)).show()


def get_ll_spn(toponym):

