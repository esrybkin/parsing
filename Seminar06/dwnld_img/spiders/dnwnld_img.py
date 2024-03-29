from typing import Any
import scrapy
from scrapy.http import HtmlResponse


class DnwnldImgSpider(scrapy.Spider):
    name = "dnwnld_img"
    allowed_domains = ["book24.ru"]
    start_urls = ["https://book24.ru/search/?q=фантастика"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f"https://book24.ru/search/?q={kwargs.get('query')}"]



    def parse(self, response:HtmlResponse):
        links = response.xpath("//div[@class='product-list__item']//a[@class='product-card__name']")
        for link in links:
            yield response.follow(link, callback=self.parse_book)
        

    
    def parse_book(self, response:HtmlResponse):
        print()
        name = response.xpath("//h1/text()").get()
        price = response.xpath("//span[@class='app-price product-sidebar-price__price/text()']").get()
        url = response.url
        