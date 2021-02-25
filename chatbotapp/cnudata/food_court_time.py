from is_vacation import get_vacation
from chatbotapp.kakaojsonformat.response import *

is_vacation = get_vacation()

def ramen_time():

    if not is_vacation:
        response_text = "🍜라면코너 운영 시간 안내🍜\n\t평일 중식 : 08:20 ~ 19:00\n\t평일 석식 : 08:20 ~ 19:00"
        answer = insert_text(response_text)
    else :
        response_text = "🍜라면코너 운영 시간 안내🍜\n\t토요일 11:00 ~ 14:30 \n\t 토요일은 사정에 따라 코너별 운영이 변동 될 수 있습니다."
        answer = insert_text(response_text)
    reply = make_reply("👉다른코너 운영 시간", "운영시간")
    answer = insert_replies(answer, reply)
    reply = make_reply("👉푸드코트 메뉴 보기", "제1학생회관")
    answer = insert_replies(answer, reply)
    reply = make_reply("👉다른식당 메뉴 보기", "학식")
    answer = insert_replies(answer, reply)

    return answer


