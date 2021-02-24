from chatbotapp.kakaojsonformat.response import *
from chatbotapp.cnudata.studenthall1_info import *

def get_entire_cafeteria_answer():
    response_text = "\n😋 충남대학교 학식 정보 😋    \n 원하시는 식당을 아래에서\n\t  선택해주세요"
    answer = insert_text(response_text)
    reply = make_reply("제1학생회관", "제1학생회관")
    answer = insert_replies(answer, reply)
    reply = make_reply("제2학생회관(인재개발원)", "제2학생회관(인재개발원)")
    answer = insert_replies(answer, reply)
    reply = make_reply("제3학생회관", "제3학생회관")
    answer = insert_replies(answer, reply)
    reply = make_reply("제4학생회관", "제4학생회관")
    answer = insert_replies(answer, reply)
    reply = make_reply("생활과학대학", "생활과학대학")
    answer = insert_replies(answer, reply)
    reply = make_reply("기숙사식당", "기숙사식당")
    answer = insert_replies(answer, reply)

    return answer

def get_studenthall1_answer():
    answer = category()
    return answer

def get_ramen_answer():
    answer = ramen()
    return answer

def get_gansik_answer():
    answer = ramen()
    return answer

def get_america_answer():
    answer = ramen()
    return answer

def get_snack_answer():
    answer = ramen()
    return answer

def get_korea_answer():
    answer = ramen()
    return answer

def get_japan_answer():
    answer = ramen()
    return answer

def get_china_answer():
    answer = ramen()
    return answer