from pytimekr import pytimekr
from datetime import date
import datetime
from chatbotapp.common.kakaojsonformat import *

holiday_list = pytimekr.holidays()  # holidays메소드는 리스트 형태로 관련값 반환


def is_holiday():
    result = False
    weekno = datetime.datetime.today().weekday()
    for holiday in holiday_list:
        if holiday == date.today() or weekno > 4:
            result = True
        else:
            pass
    return result


def insert_multiple_reply(answer, replies):
    for label, real in replies:
        tempReply = make_reply(label, real)
        answer = insert_replies(answer, tempReply)

    return answer
