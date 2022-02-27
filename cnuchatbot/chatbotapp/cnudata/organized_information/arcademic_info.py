from bs4 import BeautifulSoup
import requests
from chatbotapp.common.kakaojsonformat import *


def get_arcademic_answer():
    url = "https://plus.cnu.ac.kr/_prog/_board/?code=sub07_0702&site_dvs_cd=kr&menu_dvs_cd=0702"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
    trs = soup.find("tbody").find_all("tr")
    # print(trs)
    front_url = "https://plus.cnu.ac.kr/_prog/_board/"
    titles = [tr.find("td", attrs={"class": "title"}).get_text() for tr in trs]
    dates = [tr.find("td", attrs={"class": "date"}).get_text() for tr in trs]
    urls = [front_url + tr.find("td", attrs={"class": "title"}).a["href"] for tr in trs]

    answer = list_card("충남대학교 학사정보", titles[0], dates[0], urls[0])
    for i in range(1, 5):
        a = make_item(titles[i], dates[i], urls[i])
        answer['template']['outputs'][0]['listCard']['items'].append(a)

    return answer

