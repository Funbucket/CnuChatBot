from bs4 import BeautifulSoup
import requests, re
from chatbotapp.kakaojsonformat.response import *
from datetime import datetime
from chatbotapp.cnudata.is_vacation import get_vacation


def get_crawled_data():
    url = "https://clicker.cnu.ac.kr/Clicker/k/"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    tds = soup.find("tbody").find_all("td", attrs={"class" : re.compile("^clicker")})
    data = [i.get_text().strip() for i in tds]
    return data


def library_json_format_total():
    data = get_crawled_data()
    # value 값
    value = []
    for i in range(11):
        value.append(" 잔여좌석:" + data[4 * i + 2])

    # dict 생성
    library_info = {}
    for i in range(11):
        library_info[data[4 * i]] = value[i]
    return library_info


def library_json_format_each():
    data = get_crawled_data()
    # value 값
    value = []
    for i in range(11):
        value.append("총 좌석:" + data[4 * i + 1] + " 잔여좌석:" + data[4 * i + 2] + " [" + data[4 * i + 3] + "]")

    # dict 생성
    library_info = {}
    for i in range(11):
        library_info[data[4 * i]] = value[i]
    return library_info


# 열람실처음 눌럿을때
def get_library_answer():
    name = []
    library_info = library_json_format_total()
    now_hour = datetime.now().hour
    if get_vacation() or now_hour <= 6 or now_hour >= 22:
        response_text = "😋 충남대학교도서관 개관시간 😋\n\n"
        response_text += "[신문열람실] : 07:00~22:00 토,일휴실\n\n"
        response_text += "[전자정보실,제1자료실,제2자료실,대출실]\n"
        response_text += "09:00~18:00 토,일휴실\n\n"
        response_text += "[열람실] : 07:00~22:00 토,일휴실\n"
        for key in library_info:
            name.append(key)

    else:
        response_text = "\n😋 충남대학교 열람실 좌석 정보 😋    \n"
        for key in library_info:
            response_text += "\n👉" + key + "\n\t" + library_info[key] + "\n"
            name.append(key)
    answer = insert_text(response_text)
    reply = make_reply("🗺️층별지도보기🗺️", "층별지도보기")
    answer = insert_replies(answer, reply)
    for room_name in name:
        reply = make_reply(room_name,room_name)
        answer = insert_replies(answer,reply)
    return answer

# 한개씩 눌렀을때
def each_get_library_answer(room):
    name = []
    response_text = "\n😛 선택하신 열람실 좌석 정보 😛 \n "
    library_info = library_json_format_each()
    for key in library_info:
        name.append(key)
    if len(room) > 0:
        response_text += "\n" + room + "\n" + library_info[room]

    answer = insert_text(response_text)

    reply = make_reply("🗺️층별지도보기🗺️", "층별지도보기")
    answer = insert_replies(answer, reply)
    for room_name in name:
        reply = make_reply(room_name, room_name)
        answer = insert_replies(answer, reply)

    return answer


def each_get_library_image(floor):
    floor = floor[:-6]  # 뒤에 층별지도보기 글씨 자름 url 에 넣기위해
    if len(floor) > 2:
        floor = int(floor[2]) - 1

    answer = insert_image("https://library.cnu.ac.kr/image/ko/local/guide/floor{}.png".format(floor), floor)
    reply = make_reply("열람실 좌석보기", "열람실")
    answer = insert_replies(answer, reply)
    reply = make_reply("다른층 지도보기", "층별지도보기")
    answer = insert_replies(answer, reply)

    return answer


def entire_floor_image():
    answer = insert_text("🗺보고싶은 층을🗺 \n\t  선택해주세요\n")
    reply = make_reply("B2층", "B2층 지도보기")
    answer = insert_replies(answer, reply)
    reply = make_reply("B1층", "B1층 지도보기")
    answer = insert_replies(answer, reply)
    reply = make_reply("별관1층", "별관1층 지도보기")
    answer = insert_replies(answer, reply)

    for i in range(1,6):
        reply = make_reply("{}층".format(i), "{}층 지도보기".format(i))
        answer = insert_replies(answer, reply)

    return answer


