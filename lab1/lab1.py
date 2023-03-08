from requests import get
from bs4 import BeautifulSoup
import time


BASE_URL = "https://lpnu.ua"
HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}
FILE_NAME = "lab1.txt"
with open(FILE_NAME, "w", encoding="utf-8") as file:

    page = get(BASE_URL, headers=HEADERS)
    soup = BeautifulSoup(page.content,  "html.parser")
    inst_list = soup.find(class_="navbar-nav").find("li").find_next_sibling()
    for li in inst_list.find_all("li"):
        a = li.find("a")
        inst_name = a.find(string=True, recursive=False)
        inst_url = BASE_URL + a.get("href")
        file.write(f"Назва інститута: {inst_name}\n")
        inst_page = get(inst_url, headers=HEADERS)
        soup = BeautifulSoup(inst_page.content, "html.parser")
        dep_list = soup.find(class_="block-views-blockgroup-subgroups-block-2")
        time.sleep(0.01)
        if dep_list:
            dep_list = dep_list.find("ul")
            for li in dep_list.find_all("li"):
                a = li.find("a")
                dep_name = a.find(string=True, recursive=False)
                dep_url = a.get("href")
                file.write(f"   Назва кафедри: {dep_name}\n")
                # dep_page = get(dep_url, headers=HEADERS)
                # soup = BeautifulSoup(dep_page.content,  "html.parser")
                # staff_list = soup.find(class_ = "field--name-field-contact-person")
                # time.sleep(0.01)
                # if staff_list:
                #     div = staff_list.find("div")
                #     staff_name = div.find(string=True, recursive=False)
                #     time.sleep(0.01)
                #     file.write(f"       {staff_name}\n")
