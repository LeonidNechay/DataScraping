import scrapy
from bs4 import BeautifulSoup
from lab3.items import InstituteItem
from lab3.items import DepartmentItem
import time

class LpnuSpider(scrapy.Spider):
    name = "lpnu"
    allowed_domains = ["lpnu.ua"]
    start_urls = ["http://lpnu.ua"]
    

    def parse(self, response):
        soup = BeautifulSoup(response.body,  "html.parser")

        
        inst_list = soup.find(class_="navbar-nav").find("li").find_next_sibling()
        for li in inst_list.find_all("li"):
            a = li.find("a")
            inst_name = a.find(string=True, recursive=False)
            inst_url = f"http://lpnu.ua{a.get('href')}"
            
            yield InstituteItem(
                inst_name = inst_name,
                url = inst_url
            )
            yield scrapy.Request(
                url = inst_url,
                callback = self.parse_dep,
                meta = {
                    "Institute": inst_name
                }
            )

    def parse_dep(self, response):
        soup = BeautifulSoup(response.body,  "html.parser")

        dep_list = soup.find(class_="block-views-blockgroup-subgroups-block-2")
        inst_img = soup.find(class_="img-responsive").get("src")
        yield InstituteItem(
            img_url = [f"https://lpnu.ua{inst_img}"]
        )
        time.sleep(0.01)
        if dep_list:
            dep_list = dep_list.find("ul")
            for li in dep_list.find_all("li"):
                a = li.find("a")
                dep_name = a.find(string=True, recursive=False)
                dep_url = a.get("href")

                
                yield DepartmentItem(
                    dep_name = dep_name,
                    url = dep_url,
                    institute = response.meta.get("Institute")
                )