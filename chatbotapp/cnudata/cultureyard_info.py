from bs4 import BeautifulSoup
import requests
from chatbotapp.kakaojsonformat.response import *


def get_cultureyard_answer():
    url = "https://plus.cnu.ac.kr/_prog/_board/?code=sub07_070801&site_dvs_cd=kr&menu_dvs_cd=070801"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')

    trs = soup.find("tbody").find_all("tr")
    nums_gongzi = len(soup.find_all(string="공지\xa0"))
    front_url = "https://plus.cnu.ac.kr/_prog/_board/"

    titles = [tr.find("td", attrs={"class": "title"}).get_text()[:-1] for tr in trs[nums_gongzi:]]
    dates = [tr.find("td", attrs={"class": "date"}).get_text()[:-1] for tr in trs[nums_gongzi:]]
    urls = [front_url + tr.find("td", attrs={"class": "title"}).a["href"] for tr in trs[nums_gongzi:]]

    answer = list_card("충남대학교 문화마당", titles[0], dates[0], urls[0])

    for i in range(1, 5):
        a = make_item(titles[i], dates[i], urls[i])
        answer['template']['outputs'][0]['listCard']['items'].append(a)

    return answer


# import requests
# from bs4 import BeautifulSoup
#
# url = "https://plus.cnu.ac.kr/_prog/_board/?code=sub07_070801&site_dvs_cd=kr&menu_dvs_cd=070801"
# res = requests.get(url)
# res.raise_for_status()
# soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
#
# trs = soup.find("tbody").find_all("tr")
#
# # with open("test.html", "w", encoding="utf-8") as f:
# #     f.write(soup.prettify())
#
# def get_subtitles():
#     tds = []
#     titles = []
#     for tr in trs[2:]:
#         tds.append(tr.find("td", attrs={"class": "title"}))
#     for td in tds:
#         titles.append(td.get_text()[:-1])
#     return titles
# print(get_subtitles())
#
# def get_dates():
#     dates = []
#     str_dates = []
#     for tr in trs[2:]:
#         dates.append(tr.find("td", attrs={"class": "date"}))
#     for date in dates:
#         str_dates.append(date.get_text()[:-1])
#     return str_dates
#
#
# def get_urls():
#     tds = []
#     urls = []
#     for tr in trs[2:]:
#         tds.append(tr.find("td", attrs={"class": "title"}))
#     for td in tds:
#         urls.append("https://plus.cnu.ac.kr/_prog/_board/" + td.a["href"])
#     return urls
#
# # print(get_subtitles()[0])
# def get_cultureyard_answer():
#     answer = {
#         "version": "2.0",
#         "template": {
#             "outputs": [
#                 {
#                     "listCard": {
#                         "header": {
#                             "title": "충남대학교 문화마당"
#                         },
#                         "items": [
#                             {
#                                 "title": get_subtitles()[0],
#                                 "description": get_dates()[0],
#                                 "imageUrl": None,
#                                 "link": {
#                                     "web": get_urls()[0]
#                                 }
#                             },
#                             {
#                                 "title": get_subtitles()[1],
#                                 "description": get_dates()[1],
#                                 "imageUrl": None,
#                                 "link": {
#                                     "web": get_urls()[1]
#                                 }
#                             },
#                             {
#                                 "title": get_subtitles()[2],
#                                 "description": get_dates()[2],
#                                 "imageUrl": None,
#                                 "link": {
#                                     "web": get_urls()[2]
#                                 }
#                             },
#                             {
#                                 "title": get_subtitles()[3],
#                                 "description": get_dates()[3],
#                                 "imageUrl": None,
#                                 "link": {
#                                     "web": get_urls()[3]
#                                 }
#                             },
#                             {
#                                 "title": get_subtitles()[4],
#                                 "description": get_dates()[4],
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
