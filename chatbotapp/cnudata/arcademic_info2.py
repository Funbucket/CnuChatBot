from bs4 import BeautifulSoup
import requests
from chatbotapp.kakaojsonformat.response import *

url = "https://plus.cnu.ac.kr/_prog/_board/?code=sub07_0702&site_dvs_cd=kr&menu_dvs_cd=0702"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
trs = soup.find("div", attrs={"class": "board_list"}).find_all("tr")
# print(trs)
front_url = "https://plus.cnu.ac.kr/_prog/_board/"
titles = [tr.find("td", attrs={"class": "title"}).get_text() for tr in trs]
dates = [tr.find("td", attrs={"class": "date"}).get_text() for tr in trs]
urls = [front_url + tr.find("td", attrs={"class": "title"}).a["href"] for tr in trs]

print(titles)
print(dates)
print(urls)
