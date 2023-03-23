import scrapy
from lab2.items import InstituteItem
from lab2.items import DepartmentItem
import time

class LpnuSpider(scrapy.Spider):
    name = "lpnu_css"
    allowed_domains = ["lpnu.ua"]
    start_urls = ["http://lpnu.ua"]
    

    def parse(self, response):
        inst_list = response.css('ul.navbar-nav').css('li:nth-of-type(2)').css('a.institutes ~ ul>li')
        print(inst_list)
        for li in inst_list:
            a = li.css('a::attr(href)').get()
            inst_name = li.css('a::text').get()
            inst_url = f"http://lpnu.ua{a}"
            
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
        dep_list = response.css('section.block-views-blockgroup-subgroups-block-2').css('div.item-list').css('ul>li')
        print(dep_list)
        time.sleep(0.01)
        if dep_list:
            for li in dep_list:
                a = li.css('a::attr(href)').get()
                dep_name = li.css('a::text').get()
                dep_url = a

                yield DepartmentItem(
                    dep_name = dep_name,
                    url = dep_url,
                    institute = response.meta.get("Institute")
                )