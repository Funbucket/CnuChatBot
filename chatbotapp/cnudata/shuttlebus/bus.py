from chatbotapp.kakaojsonformat.response import *
from chatbotapp.cnudata.shuttlebus.a_line_location import get_a1_answer
from chatbotapp.cnudata.shuttlebus.a_line_2_location import get_a2_answer
from chatbotapp.cnudata.shuttlebus.b_line_location import get_b1_answer
from chatbotapp.cnudata.shuttlebus.b_line_2_location import get_b2_answer
from chatbotapp.cnudata.shuttlebus.b_line_3_location import get_b3_answer


def get_root_answer():
    answer = insert_text("충남대학교 셔틀 정보")

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
    reply = make_reply("C노선표", "C노선표")
    answer = insert_replies(answer, reply)
    return answer


def get_aroot_answer():
    text = get_a1_answer() + "\n\n"
    text += get_a2_answer()
    answer = insert_text(text)

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
    reply = make_reply("C노선표", "C노선표")
    answer = insert_replies(answer, reply)

    return answer


def get_broot_answer():
    text = get_b1_answer() + "\n\n"
    text += get_b2_answer() + "\n\n"
    text += get_b3_answer()

    answer = insert_text(text)

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
    reply = make_reply("C노선표", "C노선표")
    answer = insert_replies(answer, reply)
    # reply = make_reply("A노선표", "A노선표")
    # answer = insert_replies(answer, reply)
    # reply = make_reply("B노선표", "B노선표")
    # answer = insert_replies(answer, reply)
    # reply = make_reply("C노선표", "C노선표")
    # answer = insert_replies(answer, reply)
    return answer

    
def get_croot_answer():
    answer = insert_text(
        "대덕 ➜ 보운: 8:00, 10:00, 13:00, 17:30\n보운 ➜ 대덕: 8:50, 10:30, 13:30, 18:10\n\n노선 : 대덕캠퍼스 골프연습장 주차장 ➜ 보운캠퍼스(문화동) ➜ 대덕캠퍼스 골프연습장 주차장"
    )
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
    reply = make_reply("C노선표", "C노선표")
    answer = insert_replies(answer, reply)
    return answer


def get_croot_am_answer():
    answer = insert_text("대덕캠퍼스 ➜ 보운캠퍼스: 8:00, 10:00\n보운캠퍼스 ➜ 대덕캠퍼스: 8:50, 10:30")
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
    reply = make_reply("C노선표", "C노선표")
    answer = insert_replies(answer, reply)
    return answer


def get_croot_pm_answer():
    answer = insert_text("대덕캠퍼스 ➜ 보운캠퍼스: 13:00, 17:30\n보운캠퍼스 ➜ 대덕캠퍼스: 13:30, 18:10")
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
    reply = make_reply("C노선표", "C노선표")
    answer = insert_replies(answer, reply)
    return answer


def get_aroot_image():
    answer = insert_image("https://ifh.cc/g/ZPHixh.jpg","aroot")
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
    reply = make_reply("C노선표", "C노선표")
    answer = insert_replies(answer, reply)
    return answer


def get_broot_image():
    answer = insert_image("https://ifh.cc/g/9jr8yk.jpg","broot")
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
    reply = make_reply("C노선표", "C노선표")
    answer = insert_replies(answer, reply)
    return answer


def get_croot_image():
    answer = insert_image("https://ifh.cc/g/LPadLj.jpg","broot")
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
    reply = make_reply("C노선표", "C노선표")
    answer = insert_replies(answer, reply)
    return answer


def get_holiday_bus_answer():
    text = "주말 및 공휴일은\n셔틀운행을 하지 않습니다.\n"
    # text += "[A노선 평일첫차] : 08:30\n[B노선 평일첫차] : 08:30"
    answer = insert_text(text)
    '''reply = make_reply("A노선표", "A노선표")
    answer = insert_replies(answer, reply)
    reply = make_reply("B노선표", "B노선표")
    answer = insert_replies(answer, reply)
    reply = make_reply("C노선표", "C노선표")
    answer = insert_replies(answer, reply)'''
    # reply = make_reply("C노선", "C노선")
    # answer = insert_replies(answer, reply)
    return answer
