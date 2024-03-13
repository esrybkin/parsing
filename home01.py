# Сценарий Foursquare
# Напишите сценарий на языке Python, который предложит пользователю ввести интересующую его категорию (например, кофейни, музеи, парки и т.д.).
# Используйте API Foursquare для поиска заведений в указанной категории.
# Получите название заведения, его адрес и рейтинг для каждого из них.
# Скрипт должен вывести название и адрес и рейтинг каждого заведения в консоль.

import requests
import json

# Ваши учетные данные API
client_id = "QMK1IDEHBFD33AR1T0ESLVSPILPVTRZPADVFLF4ONZP53124"
client_secret = "TQAQOKIHC0KQMHR1IXT3V3U5IGGGLETCS4KHHB2YBOQLMTNK"

# Конечная точка API
endpoint = "https://api.foursquare.com/v3/places/search"

# Определение параметров для запроса API
# query = input("Введите название города: ")
params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "query": "cofee"
    # "fields": "rating"
}

headers = {
    "Accept": "application/json",
    "Authorization": "fsq3M4EZFyXDK54gHB6cn7W6mkoqxrHHpnAsRXDFgIeZkyo="
}

# Отправка запроса API и получение ответа
response = requests.get(endpoint, params=params,headers=headers)

# Проверка успешности запроса API
if response.status_code == 200:
    print("Успешный запрос API!")
    data = json.loads(response.text)
    venues = data["results"]
    for venue in venues:
        print("Название:", venue["name"])
        print("Адрес:", venue["location"]["address"])
        print("fsq_id:", venue["fsq_id"])
        print("Страна:", venue["location"]["country"])
        # print("Рейтинг", venue["fields"]["rating"])
        print("\n")
else:
    print("Запрос API завершился неудачей с кодом состояния:", response.status_code)
    print(response.text)

    # не могу понять в чём ошибка, рейтинг не выводится. некоторые другие поля выводит, а рейтинг нет. в Постмане тоже не получается вывести рейтинг именно у заведения, выводится список рейтингов.
