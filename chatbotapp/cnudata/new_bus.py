from chatbotapp.kakaojsonformat.response import *
from chatbotapp.cnudata.a_line_location import get_a1_answer
from chatbotapp.cnudata.a_line_2_location import get_a2_answer


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
