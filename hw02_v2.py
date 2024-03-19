# Выполнить скрейпинг данных в веб-сайта http://books.toscrape.com/
# и извлечь информацию о всех книгах на сайте во всех категориях:
# название, цену, количество товара в наличии (In stock (19 available)) в формате integer, описание.

# Затем сохранить эту информацию в JSON-файле.

from bs4 import BeautifulSoup
import requests
import pandas as pd
import urllib.parse
import re
import json

# website = "http://books.toscrape.com/"

# page = requests.get(website)
# soup = BeautifulSoup(page.content, 'html.parser')

# result = soup.find_all('li', ('class','col-xs-6 col-sm-4 col-md-3 col-lg-3'))

book_title = []
book_price = []
book_count = []
count_page = 1

url = 'https://books.toscrape.com/catalogue/page-1.html'
url_1 = "http://books.toscrape.com/catalogue/"

while True:
    url_2 = []    

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    next_page = soup.find('li', ('class', 'next'))

    try:
        next_page_link = next_page.find('a')['href']
    except:
        break

    result = soup.find_all('li', ('class','col-xs-6 col-sm-4 col-md-3 col-lg-3'))

    for i in result:
        for link in i.find_all('div', ('class', "image_container")):
            url_2.append(link.find('a').get('href'))

    url_joined = []
    for link in url_2:
        url_joined.append(urllib.parse.urljoin(url_1, link))

    # Цикл по списку ссылок на товары
    for i in url_joined:
        response = requests.get(i)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Парсинг названия товара. Обработка исключения: добавляем пустую строку.
        try:
            book_title.append(soup.find('div', ('class', 'col-sm-6 product_main')).find('h1').text)
        except:
            book_title.append('')

        # Парсинг цены товара.
        try:
            p = soup.find('p',('class','price_color')).text
            p = float(re.sub(r'[^\d.]+', '', p))
            book_price.append(p)
        except:
            book_price.append('')


        # Парсинг количества товара.
        try:
            book_count.append(soup.find('p', ('class', 'instock availability')).get_text(strip=True)[10:-1])
        except:
            book_count.append('')
    
    # if next_page == None:
    #     break

    url = url_1 + next_page_link
    
    print(f"Обработана {count_page} страница")
    count_page += 1

# Записываем данные в словарь
output = {'Title' : book_title, 'Price' : book_price, 'Available' : book_count}

# df = pd.DataFrame(output)
# print(df)

with open("data_file.json", "w") as write_file:
    json.dump(output, write_file)


