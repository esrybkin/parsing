from scrapy.crawler import CrawlerProcess
from scrapy.utils.reactor import install_reactor
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from dwnld_img.spiders.dnwnld_img import DnwnldImgSpider


if __name__ == '__main__':
    install_reactor('twisted.internet.asyncioreactor.AsincioSelectorREactor')
    configure_logging()
    process = CrawlerProcess(get_project_settings())
    # user_query = input('Введи запрос')
    # process.crawl(DnwnldImgSpider, query=user_query)
    process.crawl(DnwnldImgSpider, query='фантастика')
    process.start()