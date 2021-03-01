from bs4 import BeautifulSoup
import requests, re
from chatbotapp.kakaojsonformat.response import *

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
        value.append("잔여좌석:" + data[4 * i + 2])

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
    response_text = "\n😋 충남대학교 열람실 좌석 정보 😋    "

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
    if len(room) > 18 :
        response_text += "\t" + room + "\n" + library_info[room] + "\n"
    elif len(room) > 16 :
        response_text += "\t\t" + room + "\n" + library_info[room] + "\n"
    elif len(room) >= 14 :
        response_text += "\t\t" + room + "\n" + library_info[room] + "\n"
    elif len(room) > 0 :
        response_text += "\t\t" + room + "\n" + library_info[room] + "\n"
    answer = insert_text(response_text)

    reply = make_reply("🗺️층별지도보기🗺️", "층별지도보기")
    answer = insert_replies(answer, reply)
    for room_name in name:
        reply = make_reply(room_name, room_name)
        answer = insert_replies(answer, reply)

    return answer
print(len("2층 제 3열람실 노트북실"))
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


