import scrapy
from bs4 import BeautifulSoup
from mkr2.SeleniumRequest import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions 
from mkr2.items import ConsoleItem

class EkatalogSpider(scrapy.Spider):
    name = "ekatalog"
    allowed_domains = ["ek.ua"]
    start_urls = ["https://ek.ua/ua/list/33/"]

    def start_requests(self):   
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=10
            )

    def parse(self, response):
        soup = BeautifulSoup(response.body,  "html.parser")
        
        consoles = soup.find(id = 'list_form1').find_all(class_ = 'model-short-div')
        
        for console in consoles:
            
            if(console):
                name  = console.find(class_ = 'u').find(string=True, recursive=False)
            
                img_url = console.find(class_ = 'list-img').find(name='img').get('src')
             
                shops = console.find(class_ = 'model-hot-prices').find_all('tr')

                for shop in shops:
                
                    shop_name = shop.find(class_ = 'model-shop-name').find(name = 'u').find(string=True, recursive=False)
                    
                    shop_price = int(shop.find(class_ = 'model-shop-price').find(name = 'a').find(string=True, recursive=False).replace('\xa0', '').replace('грн.', ''))
                    
                    yield ConsoleItem(
                        name = name,
                        image_urls = [img_url],
                        shop = shop_name,
                        price = shop_price
                    )
