from bs4 import BeautifulSoup
import requests, re
from chatbotapp.common.kakaojsonformat import *
from datetime import datetime
from chatbotapp.cnudata.is_vacation import get_vacation
from chatbotapp.common.variables.library import *
from chatbotapp.models import *
from chatbotapp.common.functions import *


def get_crawled_data():
    url = library_BASE_URL
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    tds = soup.find("tbody").find_all("td", attrs={"class": re.compile("^clicker")})
    data = [i.get_text().strip() for i in tds]
    return data


def library_json_format_total():
    data = get_crawled_data()
    # value 값
    value = []
    for i in range(11):
        value.append("잔여좌석:" + data[4 * i + 2])

    # dict 생성
    library_info = {}
    for i in range(11):
        library_info[data[4 * i]] = value[i]
    return library_info


# 열람실처음 눌럿을때
def get_library_answer():
    name = []
    library_info = library_json_format_total()
    now_hour = datetime.datetime.now().hour

    # db 에서 library 에 대한 정보를 가져와줍니다
    db = Library.objects.all()[0]
    if is_holiday() or now_hour < db.normalStartTime or now_hour > db.normalEndTime:
        response_text = db.closedNotice
        for key in library_info:
            name.append(key)
    else:
        response_text = db.normalNotice
        for key in library_info:
            response_text += "\n" + "[" + key + "]" + "\n" + library_info[key] + "\n"
            name.append(key)
    answer = insert_text(response_text)
    reply = make_reply("층별지도보기", "층별지도보기")
    answer = insert_replies(answer, reply)

    return answer


def each_get_library_image(floor):
    floor = floor[:-6]  # 뒤에 층별지도보기 글씨 자름 url 에 넣기위해
    if len(floor) > 2:
        floor = int(floor[2]) - 1

    answer = insert_image("{0}{1}.png".format(libraryImage_BASE_URL, floor), floor)
    answer = insert_multiple_reply(answer, [["열람실 좌석보기", "열람실"], ["다른층 지도보기", "층별지도보기"]])

    return answer


def entire_floor_image():
    answer = insert_text("층별 지도 정보\n")

    for floor in floorImages:
        reply = make_reply(floor[:-5], floor)
        answer = insert_replies(answer, reply)

    return answer
