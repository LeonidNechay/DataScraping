import scrapy
from lab2.items import InstituteItem
from lab2.items import DepartmentItem
import time

class LpnuSpider(scrapy.Spider):
    name = "lpnu_xpath"
    allowed_domains = ["lpnu.ua"]
    start_urls = ["http://lpnu.ua"]
    

    def parse(self, response):
        inst_list = response.xpath('//ul[contains(@class, "navbar-nav")]').xpath('.//li[contains(@class, "expanded")]').xpath('.//a[contains(@class, "institutes")]').xpath('..//ul/*')
        print(inst_list)
        for li in inst_list:
            a = li.xpath('.//a/@href()').get()
            inst_name = li.xpath('.//a/text()').get()
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
        dep_list = response.xpath('//section[contains(@class, "block-views-blockgroup-subgroups-block-2")]').xpath('.//div[contains(@class, "item-list")]').xpath('.//ul/*')
        print(dep_list)
        time.sleep(0.01)
        if dep_list:
            for li in dep_list:
                a = li.xpath('.//a/@href()').get()
                dep_name = li.xpath('.//a/text()').get()
                dep_url = a

                yield DepartmentItem(
                    dep_name = dep_name,
                    url = dep_url,
                    institute = response.meta.get("Institute")
                )