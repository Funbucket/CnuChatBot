from pytimekr import pytimekr
from datetime import date, datetime
import datetime
from chatbotapp.common.kakaojsonformat import *
import json

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


"""
사용자가 보낸 kakao json format에서 utterance만 추출하여 반환한다. 
"""
def get_req(req):
    req = json.loads(req.body.decode("utf-8"))
    return req["userRequest"]["utterance"]
