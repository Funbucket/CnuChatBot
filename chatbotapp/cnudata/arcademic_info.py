import requests
from bs4 import BeautifulSoup


url = "https://plus.cnu.ac.kr/_prog/_board/?code=sub07_0702&site_dvs_cd=kr&menu_dvs_cd=0702"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')

info_list = soup.find("div", attrs={"class": "board_list"}).find_all("tr")

url_info = []
for info in info_list[1:]:
    url_info.append(info.find("td", attrs={"class": "title"}))


def get_days():
    dates = []
    days = []
    for info in info_list[1:]:
        dates.append(info.find("td", attrs={"class": "date"}))
    for date in dates:
        days.append(date.get_text())
    return days


def get_urls():
    urls = []
    for i in range(len(url_info)):
        url = url_info[i].a["href"]
        urls.append("https://plus.cnu.ac.kr/_prog/_board/" + url)
    return urls


def get_subtitles():
    subtitles = []
    for i in range(len(url_info)):
        subtitles.append(url_info[i].get_text())
    return subtitles


def get_arcademic_answer():
    answer = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "충남대학교 학사정보"
                        },
                        "items": [
                            {
                                "title": get_subtitles()[0],
                                "description": get_days()[0],
                                "imageUrl": None,
                                "link": {
                                    "web": get_urls()[0]
                                }
                            },
                            {
                                "title": get_subtitles()[1],
                                "description": get_days()[1],
                                "imageUrl": None,
                                "link": {
                                    "web": get_urls()[1]
                                }
                            },
                            {
                                "title": get_subtitles()[2],
                                "description": get_days()[2],
                                "imageUrl": None,
                                "link": {
                                    "web": get_urls()[2]
                                }
                            }
                        ],
                        "buttons": [
                            {
                                "label": "구경가기",
                                "action": "webLink",
                                "webLinkUrl": "https://namu.wiki/w/%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%94%84%EB%A0%8C%EC%A6%88"
                            }
                        ]
                    }
                }
            ]
        }
    }
    return answer
