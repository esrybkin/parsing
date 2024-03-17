# Выполнить скрейпинг данных в веб-сайта http://books.toscrape.com/
# и извлечь информацию о всех книгах на сайте во всех категориях:
# название, цену, количество товара в наличии (In stock (19 available)) в формате integer, описание.

# Затем сохранить эту информацию в JSON-файле.

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import urllib.parse

ua = UserAgent()

url = "https://books.toscrape.com/"

headers = {"UserAgent": ua.chrome}
# params = {"page":1}
# page = 1
session = requests.session()

all_books = []

response = session.get(url, headers=headers)
soup = BeautifulSoup(response.text, features="html.parser")
books = soup.find_all('li', {'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})

# Вывод ссылок на
release_links = []
for link in soup.find_all('div', {'class', 'image_container'}):
    release_links.append(link.find('a').get('href'))

# Объединение ссылок с базовым URL-адресом для создания списка URL-адресов
url_joined = []
for link in release_links:
  url_joined.append(urllib.parse.urljoin(url + "/catalogue", link))

for book in books:
    book_title = book.h3.a["title"]
    book_price = book.find("p", {"class": "price_color"})
    price = book_price[0].text.strip()

    print("Title of the book :" + book_title)
    print("Price of the book :" + price)
    # print(f"Обработана {page} страница")
    # page += 1
# print(all_books)

# print(book_title)

