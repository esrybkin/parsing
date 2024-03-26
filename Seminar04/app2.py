import requests
from lxml import html
from pymongo import MongoClient

def insert_to_db(list_movies):
    client = MongoClient("mongodb://localhost:27017")
    db = client['imdb_movies']
    collection = db["top_movies"]
    collection.insert_many(list_movies)

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
resp = requests.get(url=url, headers=headers)

tree = html.fromstring(html = resp.content)

movies = tree.xpath("//table[@]")