from bs4 import BeautifulSoup
import requests
from chatbotapp.kakaojsonformat.response import *


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
# import requests
# from bs4 import BeautifulSoup
#
#
# url = "https://plus.cnu.ac.kr/_prog/_board/?code=sub07_0702&site_dvs_cd=kr&menu_dvs_cd=0702"
# res = requests.get(url)
# res.raise_for_status()
# soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
#
# info_list = soup.find("div", attrs={"class": "board_list"}).find_all("tr")
#
# url_info = []
# for info in info_list[1:]:
#     url_info.append(info.find("td", attrs={"class": "title"}))
#
#
# def get_days():
#     dates = []
#     days = []
#     for info in info_list[1:]:
#         dates.append(info.find("td", attrs={"class": "date"}))
#     for date in dates:
#         days.append(date.get_text())
#     return days
#
#
# def get_urls():
#     urls = []
#     for i in range(len(url_info)):
#         url = url_info[i].a["href"]
#         urls.append("https://plus.cnu.ac.kr/_prog/_board/" + url)
#     return urls
#
#
# def get_subtitles():
#     subtitles = []
#     for i in range(len(url_info)):
#         subtitles.append(url_info[i].get_text())
#     return subtitles
#
#
# def get_arcademic_answer():
#     answer = {
#         "version": "2.0",
#         "template": {
#             "outputs": [
#                 {
#                     "listCard": {
#                         "header": {
#                             "title": "충남대학교 학사정보"
#                         },
#                         "items": [
#                             {
#                                 "title": get_subtitles()[0],
#                                 "description": get_days()[0],
#                                 "imageUrl": None,
#                                 "link": {
#                                     "web": get_urls()[0]
#                                 }
#                             },
#                             {
#                                 "title": get_subtitles()[1],
#                                 "description": get_days()[1],
#                                 "imageUrl": None,
#                                 "link": {
#                                     "web": get_urls()[1]
#                                 }
#                             },
#                             {
#                                 "title": get_subtitles()[2],
#                                 "description": get_days()[2],
#                                 "imageUrl": None,
#                                 "link": {
#                                     "web": get_urls()[2]
#                                 }
#                             },
#                             {
#                                 "title": get_subtitles()[3],
#                                 "description": get_days()[3],
#                                 "imageUrl": None,
#                                 "link": {
#                                     "web": get_urls()[3]
#                                 }
#                             },
#                             {
#                                 "title": get_subtitles()[4],
#                                 "description": get_days()[4],
#                                 "imageUrl": None,
#                                 "link": {
#                                     "web": get_urls()[4]
#                                 }
#                             }
#                         ],
#                         "buttons": None
#                     }
#                 }
#             ]
#         }
#     }
#     return answer
