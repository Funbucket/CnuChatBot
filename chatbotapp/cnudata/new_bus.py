from chatbotapp.kakaojsonformat.response import *
from chatbotapp.cnudata.a_line_location import get_a1_answer
from chatbotapp.cnudata.a_line_2_location import get_a2_answer
from chatbotapp.cnudata.b_line_location import get_b1_answer
from chatbotapp.cnudata.b_line_2_location import get_b2_answer
from chatbotapp.cnudata.b_line_3_location import get_b3_answer


def get_root_answer():
    answer = insert_text("😋 충남대학교 셔틀 정보 😋\n\n원하시는 노선을선택해주세요\n도착 시간은 노선별 운행표를 기반으로 제공하므로 미리 정류장에서 기다리는 것을 권장합니다😆\n")

    reply = make_reply("A노선", "A노선")
    answer = insert_replies(answer, reply)
    reply = make_reply("B노선", "B노선")
    answer = insert_replies(answer, reply)
    reply = make_reply("C노선", "C노선")
    answer = insert_replies(answer, reply)
    reply = make_reply("A노선표", "A노선표")
    answer = insert_replies(answer, reply)
    reply = make_reply("B노선표", "B노선표")
    answer = insert_replies(answer, reply)
    return answer


def get_aroot_answer():
    text = get_a1_answer() + "\n\n"
    text += get_a2_answer()
    answer = insert_text(text)

    reply = make_reply("B노선","B노선")
    answer = insert_replies(answer, reply)
    reply = make_reply("C노선", "C노선")
    answer = insert_replies(answer, reply)
    reply = make_reply("A노선표", "A노선표")
    answer = insert_replies(answer, reply)
    reply = make_reply("B노선표", "B노선표")
    answer = insert_replies(answer, reply)

    return answer

def get_broot_answer():
    text = get_b1_answer() + "\n\n"
    text += get_b2_answer()  + "\n\n"
    text += get_b3_answer()

    answer = insert_text(text)

    reply = make_reply("A노선","A노선")
    answer = insert_replies(answer, reply)
    reply = make_reply("C노선", "C노선")
    answer = insert_replies(answer, reply)
    reply = make_reply("A노선표", "A노선표")
    answer = insert_replies(answer, reply)
    reply = make_reply("B노선표", "B노선표")
    answer = insert_replies(answer, reply)

    return answer


    
def get_croot_answer():
    answer = insert_text("🚌 1일 왕복 2회 운행(오전, 오후) 🚌\n\n노선표: 대덕캠퍼스 골프연습장 주차장 ➜ 보운캠퍼스(문화동) ➜ 대덕캠퍼스 골프연습장 주차장")
    reply = make_reply("☀오전", "오전")
    answer = insert_replies(answer, reply)
    reply = make_reply("🌙오후", "오후")
    answer = insert_replies(answer, reply)
    return answer


def get_croot_am_answer():
    answer = insert_text("대덕캠퍼스 ➜ 보운캠퍼스: 8:10\n보운캠퍼스 ➜ 대덕캠퍼스: 8:40")
    return answer


def get_croot_pm_answer():
    answer = insert_text("대덕캠퍼스 ➜ 보운캠퍼스: 17:30\n보운캠퍼스 ➜ 대덕캠퍼스: 18:00")
    return answer

def get_aroot_image():
    answer = insert_image("https://ifh.cc/g/ZPHixh.jpg","aroot")
    reply = make_reply("A노선", "A노선")
    answer = insert_replies(answer, reply)
    reply = make_reply("B노선", "B노선")
    answer = insert_replies(answer, reply)
    reply = make_reply("B노선표", "B노선표")
    answer = insert_replies(answer, reply)
    return answer


def get_broot_image():
    answer = insert_image("https://ifh.cc/g/9jr8yk.jpg","broot")
    reply = make_reply("A노선", "A노선")
    answer = insert_replies(answer, reply)
    reply = make_reply("B노선", "B노선")
    answer = insert_replies(answer, reply)
    reply = make_reply("A노선표", "A노선표")
    answer = insert_replies(answer, reply)
    return answer
