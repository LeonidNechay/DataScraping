import scrapy
from bs4 import BeautifulSoup
from mkr1.items import TabletItem

class HotlineSpider(scrapy.Spider):
    name = "hotline"
    allowed_domains = ["hotline.ua"]
    start_urls = ["https://hotline.ua/ua/computer/planshety/"]

    def parse(self, response):
        soup = BeautifulSoup(response.body,  "html.parser")
        
        tablets = soup.find(class_ = 'list-body__content').find_all(class_ = 'list-item')
        
        for tablet in tablets:
            
            name = tablet.find(class_ = 'list-item__title').find(string=True, recursive=False)
            
            url = tablet.find(class_ = 'list-item__title').get('href')
            
            price = tablet.find(class_ = 'price__value').find(string=True, recursive=False)
            
            img = f"https://hotline.ua{tablet.find(name='img').get('src')}"
            
            
            yield TabletItem(
                name=name,
                price=price,
                url=url,
                image_urls=[img]
            )
