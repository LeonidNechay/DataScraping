import scrapy
from bs4 import BeautifulSoup
from lab5.SeleniumRequest import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions 
from lab5.items import AnimeItem
import time

class AnimeSpider(scrapy.Spider):
    name = "anime"
    allowed_domains = ["animego.org"]
    start_urls = ["https://animego.org/anime?sort=r.rating&direction=desc"]
    
    def start_requests(self):   
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=10
            )
            
    def parse(self, response):
        soup = BeautifulSoup(response.body,  "html.parser")
        animeList = soup.find(id = "anime-list-container")
        for anime in animeList:
            if anime:
                name = anime.find(class_ = "h5").find("a").find(string=True, recursive=False)
                url = anime.find(class_ = "d-block").get("href")
                rank = anime.find(class_ = "animes-list-item-picture").find(class_ = "p-rate-flag__text").find(string=True, recursive=False)
                yield AnimeItem(
                        name = name,
                        url = url,
                        rank = rank
                    )
