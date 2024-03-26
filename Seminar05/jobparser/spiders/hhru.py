import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem

class HhruSpider(scrapy.Spider):
    name = "hhru"
    allowed_domains = ["hh.ru"]
    start_urls = ["https://www.labirint.ru/search/%D1%84%D0%B0%D0%BD%D1%82%D0%B0%D1%81%D1%82%D0%B8%D0%BA%D0%B0/?stype=0"]

    def parse(self, response:HtmlResponse):

        next_page = response.xpath("//a[@class='pagination-next__text']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath("//a[@class='product-card__name']/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.vacancy_parse)
    
    def vacancy_parse(self, response:HtmlResponse):
        name = response.xpath("//div[@id='product-title']/text()").get()
        price = response.xpath("//span[@class='buying-pricenew-val-number']").get()
        full_price = response.xpath("//span[@class='buying-priceold-val-number']").get()
        url = response.url
        yield JobparserItem(name=name, full_price=full_price, price=price, url=url)
