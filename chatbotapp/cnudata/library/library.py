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
    # now_hour = 10
    if get_vacation() or now_hour <= 6 or now_hour >= 22:
        response_text = "충남대학교도서관 개관시간\n\n"
        response_text += "[신문열람실]\n평일 : 07:00~22:00\n주말 및 공휴일 : 휴실\n\n"
        response_text += "[전자정보실,제1자료실,제2자료실,대출실]\n"
        response_text += "평일 : 09:00~18:00 \n주말 및 공휴일 : 휴실\n\n"
        response_text += "[열람실]\n평일 : 07:00~22:00\n주말 및 공휴일 : 휴실\n"
        for key in library_info:
            name.append(key)

    else:
        response_text = "\n충남대학교 열람실 좌석 정보\n"
        for key in library_info:
            response_text += "\n" + "[" + key + "]" + "\n" + library_info[key] + "\n"
            name.append(key)
    answer = insert_text(response_text)
    reply = make_reply("층별지도보기", "층별지도보기")
    answer = insert_replies(answer, reply)
    # for room_name in name:
    #     reply = make_reply(room_name,room_name)
    #     answer = insert_replies(answer,reply)
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

    reply = make_reply("층별지도보기", "층별지도보기")
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
    answer = insert_text("충별 지도 정보\n")
    reply = make_reply("B2층", "B2층 지도보기")
    answer = insert_replies(answer, reply)
    reply = make_reply("B1층", "B1층 지도보기")
    answer = insert_replies(answer, reply)
    reply = make_reply("별관1층", "별관1층 지도보기")
    answer = insert_replies(answer, reply)

    for i in range(1, 6):
        reply = make_reply("{}층".format(i), "{}층 지도보기".format(i))
        answer = insert_replies(answer, reply)

    return answer


def readingRoom_for_exam_week():
    answer = insert_text("시험기간 입니다. 모두 원하시는 결과 얻으시기를 츠누봇은 항상 응원합니다.")
    reply = make_reply("시험기간운영정보", "시험기간운영정보")
    answer = insert_replies(answer, reply)
    reply = make_reply("좌석정보", "좌석정보")
    answer = insert_replies(answer, reply)
    reply = make_reply("층별지도보기", "층별지도보기")
    answer = insert_replies(answer, reply)

    return answer


def exam_week_information():
    answer = insert_text(
        "중간고사기간 열람실 연장운영\n운영기간 : 4.12(월)~4.23(금)\n월~금 : 07:00 ~ 23:00\n토~일 : 09:00 ~ 23:00\n이용방법 : 마스크 착용, 발열체크 ,출입관리시스템이용")
    reply = make_reply("층별지도보기", "층별지도보기")
    answer = insert_replies(answer, reply)
    reply = make_reply("좌석정보", "좌석정보")
    answer = insert_replies(answer, reply)

    return answer


def exam_temp_get_library_answer():
    name = []
    library_info = library_json_format_total()
    now_hour = datetime.now().hour

    if now_hour <= 6 or now_hour > 23:
        answer = insert_text(
            "현재 운영시간이 아닙니다\n중간고사기간 열람실 연장운영\n운영기간:4.12(월)~4.23(금)\n월~금 : 07:00 ~ 23:00\n토~일 : 09:00 ~ 23:00\n이용방법 : 마스크 착용, 발열체크 ,출입관리시스템이용")
        return answer
    else:
        response_text = "\n😋 충남대학교 열람실 좌석 정보 😋    \n"
        for key in library_info:
            response_text += "\n👉" + key + "\n\t" + library_info[key] + "\n"
            name.append(key)
    answer = insert_text(response_text)
    reply = make_reply("층별지도보기", "층별지도보기")
    answer = insert_replies(answer, reply)
    # for room_name in name:
    #     reply = make_reply(room_name,room_name)
    #     answer = insert_replies(answer,reply)
    return answer
