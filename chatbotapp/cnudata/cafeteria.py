from chatbotapp.kakaojsonformat.response import *
from chatbotapp.cnudata.studenthall1_info import *
from chatbotapp.cnudata.studenthall2_info import make_answer_food_menu
from food_court_time import *


def get_entire_cafeteria_answer():
    response_text = "\n😋 충남대학교 학식 정보 😋   \n\t\t  원하시는 식당을 \n\t\t\t선택해주세요"
    answer = insert_text(response_text)
    reply = make_reply("🌼 제1학생회관", "제1학생회관")
    answer = insert_replies(answer, reply)
    reply = make_reply("🌼 제2학생회관(인재개발원)", "제2학생회관(인재개발원)")
    answer = insert_replies(answer, reply)
    reply = make_reply("🌼 제3학생회관", "제3학생회관")
    answer = insert_replies(answer, reply)
    reply = make_reply("🌼 제4학생회관", "제4학생회관")
    answer = insert_replies(answer, reply)
    reply = make_reply("🌼 생활과학대학", "생활과학대학")
    answer = insert_replies(answer, reply)
    reply = make_reply("🌼 기숙사식당", "기숙사식당")
    answer = insert_replies(answer, reply)

    return answer


def get_studenthall1_answer():
    answer = category()
    return answer


def get_ramen_answer():
    answer = ramen()
    return answer


def get_gansik_answer():
    answer = gansik()
    return answer


def get_america_answer():
    answer = america()
    return answer


def get_snack_answer():
    answer = snack()
    return answer


def get_korea_answer():
    answer = korea()
    return answer


def get_japan_answer():
    answer = japan()
    return answer


def get_china_answer():
    answer = china()
    return answer


def get_studenthall2345_answer(name):
    response_text = f"\n😋 충남대학교 {name} 메뉴 😋    \n "
    response_text += make_answer_food_menu(name)
    answer = insert_text(response_text)
    reply = make_reply("🌈다른 식당 메뉴보기🌈", "학식")
    answer = insert_replies(answer, reply)

    return answer


def get_ramen_time():
    answer = ramen_time()
    return answer

