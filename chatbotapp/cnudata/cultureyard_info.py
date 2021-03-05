import requests
from bs4 import BeautifulSoup

url = "https://plus.cnu.ac.kr/_prog/_board/?code=sub07_070801&site_dvs_cd=kr&menu_dvs_cd=070801"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')

trs = soup.find("tbody").find_all("tr")

# with open("test.html", "w", encoding="utf-8") as f:
#     f.write(soup.prettify())

def get_subtitles():
    tds = []
    titles = []
    for tr in trs[2:]:
        tds.append(tr.find("td", attrs={"class": "title"}))
    for td in tds:
        titles.append(td.get_text()[:-1])
    return titles
print(get_subtitles())

def get_dates():
    dates = []
    str_dates = []
    for tr in trs[1:]:
        dates.append(tr.find("td", attrs={"class": "date"}))
    for date in dates:
        str_dates.append(date.get_text()[:-1])
    return str_dates


def get_urls():
    tds = []
    urls = []
    for tr in trs[1:]:
        tds.append(tr.find("td", attrs={"class": "title"}))
    for td in tds:
        urls.append("https://plus.cnu.ac.kr/_prog/_board/" + td.a["href"])
    return urls

# print(get_subtitles()[0])
def get_cultureyard_answer():
    answer = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "충남대학교 문화마당"
                        },
                        "items": [
                            {
                                "title": get_subtitles()[0],
                                "description": get_dates()[0],
                                "imageUrl": None,
                                "link": {
                                    "web": get_urls()[0]
                                }
                            },
                            {
                                "title": get_subtitles()[1],
                                "description": get_dates()[1],
                                "imageUrl": None,
                                "link": {
                                    "web": get_urls()[1]
                                }
                            },
                            {
                                "title": get_subtitles()[2],
                                "description": get_dates()[2],
                                "imageUrl": None,
                                "link": {
                                    "web": get_urls()[2]
                                }
                            },
                            {
                                "title": get_subtitles()[3],
                                "description": get_dates()[3],
                                "imageUrl": None,
                                "link": {
                                    "web": get_urls()[3]
                                }
                            },
                            {
                                "title": get_subtitles()[4],
                                "description": get_dates()[4],
                                "imageUrl": None,
                                "link": {
                                    "web": get_urls()[4]
                                }
                            }
                        ],
                        "buttons": None
                    }
                }
            ]
        }
    }
    return answer
