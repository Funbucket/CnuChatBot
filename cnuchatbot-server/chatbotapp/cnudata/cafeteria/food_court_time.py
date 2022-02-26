from chatbotapp.cnudata.is_vacation import get_vacation
from chatbotapp.common.kakaojsonformat import *

is_vacation = get_vacation()


def entire_time():
    response_text = "[라면코너]\n운영안함\n\n[간식코너]\n운영안함\n\n[스낵코너]\n11:00 ~ 14:30\n\n[한식코너]\n11:00 ~ 14:00\n\n[일식코너]\n11:00 ~ 14:00\n\n[중식코너]\n11:00 ~ 14:30\n\n*저녁, 주말, 공휴일 운영안함"
    answer = insert_text(response_text)
    reply = make_reply("메뉴보기", "제1학생회관")
    answer = insert_replies(answer, reply)
    '''reply = make_reply("🍜라면", "라면코너 운영 시간")
    answer = insert_replies(answer, reply)
    reply = make_reply("🍙간식", "간식코너 운영 시간")
    answer = insert_replies(answer, reply)
    # reply = make_reply("🍝양식", "양식코너 운영 시간")
    # answer = insert_replies(answer, reply)
    reply = make_reply("🍔스낵", "스낵코너 운영 시간")
    answer = insert_replies(answer, reply)
    reply = make_reply("🥘한식", "한식코너 운영 시간")
    answer = insert_replies(answer, reply)
    reply = make_reply("🍣일식", "일식코너 운영 시간")
    answer = insert_replies(answer, reply)
    reply = make_reply("🥟중식", "중식코너 운영 시간")
    answer = insert_replies(answer, reply)'''

    return answer


'''def entire_time():
    response_text = "⏰\t푸드코트 운영 시간 안내\t\n\t\t\t토요일은 사정에 따라 \n코너별 운영이 변동 될 수 있습니다"
    answer = insert_text(response_text)
    reply = make_reply("🍜라면", "라면코너 운영 시간")
    answer = insert_replies(answer, reply)
    reply = make_reply("🍙간식", "간식코너 운영 시간")
    answer = insert_replies(answer, reply)
    # reply = make_reply("🍝양식", "양식코너 운영 시간")
    # answer = insert_replies(answer, reply)
    reply = make_reply("🍔스낵", "스낵코너 운영 시간")
    answer = insert_replies(answer, reply)
    reply = make_reply("🥘한식", "한식코너 운영 시간")
    answer = insert_replies(answer, reply)
    reply = make_reply("🍣일식", "일식코너 운영 시간")
    answer = insert_replies(answer, reply)
    reply = make_reply("🥟중식", "중식코너 운영 시간")
    answer = insert_replies(answer, reply)

    return answer
'''


def ramen_time():

    if not is_vacation:
        response_text = "🍜라면코너 운영 시간 안내🍜\n☀️평일 : 10:00 ~ 15:00"
        answer = insert_text(response_text)
    else:
        response_text = "🍜라면코너 운영 시간 안내🍜\n\t 토요일 10:00 ~ 15:00 \n\t 토요일은 사정에 따라 코너별 운영이 \n\t변동 될 수 있습니다."
        answer = insert_text(response_text)

    reply = make_reply("다른코너 운영 시간", "운영시간")
    answer = insert_replies(answer, reply)
    reply = make_reply("라면코너 메뉴 보기", "라면&우동")
    answer = insert_replies(answer, reply)
    reply = make_reply("푸드코트 메뉴 보기", "제1학생회관")
    answer = insert_replies(answer, reply)
    reply = make_reply("다른식당 메뉴 보기", "학식")
    answer = insert_replies(answer, reply)

    return answer


def gansik_time():

    if not is_vacation:
        response_text = "🍙간식코너 운영 시간 안내🍙\n평일 : 10:00 ~ 15:00\n"
        answer = insert_text(response_text)
    else:
        response_text = "🍙간식코너 운영 시간 안내🍙\n\t 토요일 : 10:00 ~ 15:00 \n\t 토요일은 사정에 따라 코너별 운영이 \n\t변동 될 수 있습니다."
        answer = insert_text(response_text)

    reply = make_reply("다른코너 운영 시간", "운영시간")
    answer = insert_replies(answer, reply)
    reply = make_reply("간식코너 메뉴 보기", "간식")
    answer = insert_replies(answer, reply)
    reply = make_reply("푸드코트 메뉴 보기", "제1학생회관")
    answer = insert_replies(answer, reply)
    reply = make_reply("다른식당 메뉴 보기", "학식")
    answer = insert_replies(answer, reply)

    return answer


def america_time():

    if not is_vacation:
        response_text = "🍝양식코너 운영 시간 안내🍝\n평일 중식 : 11:00 ~ 14:30\n🌙평일 석식 : 16:30 ~ 19:00\n⏳Break Time : 14:30 ~ 16:30"
        answer = insert_text(response_text)
    else :
        response_text = "🍝양식코너 운영 시간 안내🍝\n\t 토요일 11:00 ~ 14:30 \n\t 토요일은 사정에 따라 코너별 운영이 \n\t변동 될 수 있습니다."
        answer = insert_text(response_text)
        
    reply = make_reply("다른코너 운영 시간", "운영시간")
    answer = insert_replies(answer, reply)
    reply = make_reply("양식코너 메뉴 보기", "양식")
    answer = insert_replies(answer, reply)
    reply = make_reply("푸드코트 메뉴 보기", "제1학생회관")
    answer = insert_replies(answer, reply)
    reply = make_reply("다른식당 메뉴 보기", "학식")
    answer = insert_replies(answer, reply)

    return answer


def snack_time():
    if not is_vacation:
        response_text = "🍔스낵코너 운영 시간 안내🍔\n평일 : 11:00 ~ 14:30\n"
        answer = insert_text(response_text)
    else:
        response_text = "🍔스낵코너 운영 시간 안내🍔\n\t 토요일 11:00 ~ 14:30 \n\t 토요일은 사정에 따라 코너별 운영이 \n\t변동 될 수 있습니다."
        answer = insert_text(response_text)

    reply = make_reply("다른코너 운영 시간", "운영시간")
    answer = insert_replies(answer, reply)
    reply = make_reply("스낵코너 메뉴 보기", "스낵")
    answer = insert_replies(answer, reply)
    reply = make_reply("푸드코트 메뉴 보기", "제1학생회관")
    answer = insert_replies(answer, reply)
    reply = make_reply("다른식당 메뉴 보기", "학식")
    answer = insert_replies(answer, reply)

    return answer


def korea_time():
    if not is_vacation:
        response_text = "🥘한식코너 운영 시간 안내🥘\n평일 : 11:00 ~ 14:00\n"
        answer = insert_text(response_text)
    else:
        response_text = "🥘한식코너 운영 시간 안내🥘\n\t 토요일 11:00 ~ 14:00 \n\t 토요일은 사정에 따라 코너별 운영이 \n\t변동 될 수 있습니다."
        answer = insert_text(response_text)

    reply = make_reply("다른코너 운영 시간", "운영시간")
    answer = insert_replies(answer, reply)
    reply = make_reply("한식코너 메뉴 보기", "한식")
    answer = insert_replies(answer, reply)
    reply = make_reply("푸드코트 메뉴 보기", "제1학생회관")
    answer = insert_replies(answer, reply)
    reply = make_reply("다른식당 메뉴 보기", "학식")
    answer = insert_replies(answer, reply)

    return answer


def japan_time():
    if not is_vacation:
        response_text = "🍣일식코너 운영 시간 안내🍣\n평일 중식 : 11:00 ~ 14:00\n"
        answer = insert_text(response_text)
    else:
        response_text = "🍣일식코너 운영 시간 안내🍣\n\t 토요일 11:00 ~ 14:00 \n\t 토요일은 사정에 따라 코너별 운영이 \n\t변동 될 수 있습니다."
        answer = insert_text(response_text)

    reply = make_reply("다른코너 운영 시간", "운영시간")
    answer = insert_replies(answer, reply)
    reply = make_reply("일식코너 메뉴 보기", "일식")
    answer = insert_replies(answer, reply)
    reply = make_reply("푸드코트 메뉴 보기", "제1학생회관")
    answer = insert_replies(answer, reply)
    reply = make_reply("다른식당 메뉴 보기", "학식")
    answer = insert_replies(answer, reply)

    return answer


def china_time():

    if not is_vacation:
        response_text = "🥟중식코너 운영 시간 안내🥟\n평일 : 11:00 ~ 14:30\n"
        answer = insert_text(response_text)
    else:
        response_text = "🥟중식코너 운영 시간 안내🥟\n토요일 : 11:00 ~ 14:30\n\t토요일은 사정에 따라 코너별 운영이 \n\t변동 될 수 있습니다."
        answer = insert_text(response_text)

    reply = make_reply("다른코너 운영 시간", "운영시간")
    answer = insert_replies(answer, reply)
    reply = make_reply("중식코너 메뉴 보기", "중식")
    answer = insert_replies(answer, reply)
    reply = make_reply("푸드코트 메뉴 보기", "제1학생회관")
    answer = insert_replies(answer, reply)
    reply = make_reply("다른식당 메뉴 보기", "학식")
    answer = insert_replies(answer, reply)

    return answer