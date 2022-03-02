from chatbotapp.common.kakaojsonformat import *
from chatbotapp.models import ShuttleA, ShuttleB, ShuttleC
from datetime import datetime, timedelta, time, date
from typing import NamedTuple
from chatbotapp.common.functions import insert_multiple_reply

IMAGE_URL = {
   "A": "https://res.cloudinary.com/dvrcr0hkb/image/upload/v1633810851/KakaoTalk_20210912_215636605_amglsv.jpg",
   "B": "https://res.cloudinary.com/dvrcr0hkb/image/upload/v1633810851/KakaoTalk_20210904_200707497_hvhm8n.jpg",
   "C": "https://res.cloudinary.com/dvrcr0hkb/image/upload/v1633810888/KakaoTalk_20211010_051327589_t0alks.jpg"
}

"""
A : A노선 시간을 담은 배열
B : B노선 시간을 담은 배열 
CB : C노선 보운행 시간을 담은 배열
CD : C노선 대덕행 시간을 담은 배열
"""
LINE = {
    "A": ShuttleA.objects.values_list('departureTime', flat=True).distinct(),
    "B": ShuttleB.objects.values_list('departureTime', flat=True).distinct(),
    "CB": ShuttleC.objects.filter(direction="보운행").values_list('departureTime', flat=True).distinct(),
    "CD": ShuttleC.objects.filter(direction="대덕행").values_list('departureTime', flat=True).distinct()
}


"""
line_name : 노선명
prev : 직전 차량 수
next : 직후 차량 수
times : 전, 후 차량 시간
"""
class AdjTimes(NamedTuple):
    line_name_: str
    prev_: int
    next_: int
    times_: list


"""
get_datetime
time object를 인자로 받아서 오늘의 datetime object 반환
"""
def get_datetime(time):
    return datetime.combine(date.today(), time)


"""
time object를 인자로 받으면 H:M 형식의 string 반환
"""
def str_time(time):
    return time.strftime("%H:%M")

"""
두개의 time object를 인자로 받아서 차이값(절대값)을 분 단위로 반환한다.
"""
def time_diff(x, y):
    return abs(int((get_datetime(x) - get_datetime(y)).total_seconds() / 60))


"""
find_adjacent_times
노선의 이름(A, B)과 현재 시간을 인자로 받아서 AdjTimes type을 반환한다.
"""
def find_adjacent_times(line_name, cur_time):
    line_times = LINE[line_name]
    last_index = len(line_times) - 1
    """
    case 1 : 운행종료, 00시 이후 첫차 출발 30 분전 or 마지막 차량 30분 이후 24시 이전
    case 2 : 직전 0개 직후 2개, (첫차 - 30분) 이후 첫차 직전
    case 3 : 직전 1개 직후 2개, 첫차 출발 직후 두번째차 출발 직전 
    case 4 : 직전 2개 직후 1개, 마지막 두번째 차 출발 직후 마지막차 출발 직전
    case 5 : 직적 2개 직후 0개, 마지막 출발 직후
    case 6 : 직전 2개 직후 2개, 반복문 
    """
    if get_datetime(time(0)) < cur_time < get_datetime(line_times[0]) - timedelta(minutes=30) or \
       get_datetime(line_times[last_index]) + timedelta(minutes=30) < cur_time < get_datetime(time(23, 59, 59)):
        return AdjTimes(line_name, 0, 0, [line_times[0], line_times[last_index]])

    elif get_datetime(line_times[0]) - timedelta(minutes=30) <= cur_time <= get_datetime(line_times[0]):
        return AdjTimes(line_name, 0, 2, [line_times[0], line_times[1]])

    elif get_datetime(line_times[0]) < cur_time <= get_datetime(line_times[1]):
        return AdjTimes(line_name, 1, 2, [line_times[0], line_times[1], line_times[2]])

    elif get_datetime(line_times[last_index - 1]) < cur_time <= get_datetime(line_times[last_index]):
        return AdjTimes(line_name, 2, 1, [line_times[last_index - 2], line_times[last_index - 1], line_times[last_index]])

    elif get_datetime(line_times[last_index]) < cur_time:
        return AdjTimes(line_name, 2, 0, [line_times[last_index - 2], line_times[last_index - 1]])

    else:
        for index, line_time in enumerate(line_times):
            if cur_time < get_datetime(line_time):
                return AdjTimes(line_name, 2, 2, [line_times[index - 2], line_times[index - 1], line_times[index], line_times[index + 1]])


"""
AdjTimes struct와 current time을 인자로 받아서 
조건에 맞는 전, 후 차량의 시간을 string type으로 반환한다.
"""
def get_str_time_info(adj_time, cur_time):
    # datetime object -> time object
    cur_time = cur_time.time()

    # case 1
    if adj_time.prev_ == 0 and adj_time.next_ == 0:
        ret = "운행종료" + \
              "\n첫차 " + str_time(adj_time.times_[0]) + " (월평역 출발)" + \
              "\n막차 " + str_time(adj_time.times_[1])
        return ret
    # case 2
    elif adj_time.prev_ == 0 and adj_time.next_ == 2:
        ret = "[" + str(adj_time.prev_) + "대 운행중]" + \
              "\n\n" + \
              "[" + str(adj_time.next_) + "대 대기중]" + \
              "\n" + str_time(adj_time.times_[0]) + "(" + str(time_diff(adj_time.times_[0], cur_time)) + "분후)" + \
              "\n" + str_time(adj_time.times_[1]) + "(" + str(time_diff(adj_time.times_[1], cur_time)) + "분후)"
        return ret
    # case 3
    elif adj_time.prev_ == 1 and adj_time.next_ == 2:
        ret = "[" + str(adj_time.prev_) + "대 운행중]" + \
              "\n" + str_time(adj_time.times_[0]) + "(" + str(time_diff(adj_time.times_[0], cur_time)) + "분전)" + \
              "\n\n" + \
              "[" + str(adj_time.next_) + "대 대기중]" + \
              "\n" + str_time(adj_time.times_[1]) + "(" + str(time_diff(adj_time.times_[1], cur_time)) + "분후)" + \
              "\n" + str_time(adj_time.times_[2]) + "(" + str(time_diff(adj_time.times_[2], cur_time)) + "분후)"
        return ret
    # case 4
    elif adj_time.prev_ == 2 and adj_time.next_ == 1:
        ret = "[" + str(adj_time.prev_) + "대 운행중]" + \
              "\n" + str_time(adj_time.times_[0]) + "(" + str(time_diff(adj_time.times_[0], cur_time)) + "분전)" + \
              "\n" + str_time(adj_time.times_[1]) + "(" + str(time_diff(adj_time.times_[1], cur_time)) + "분전)" + \
              "\n\n" + \
              "[" + str(adj_time.next_) + "대 대기중]" + \
              "\n" + str_time(adj_time.times_[2]) + "(" + str(time_diff(adj_time.times_[2], cur_time)) + "분후)"
        return ret
    # case 5
    elif adj_time.prev_ == 2 and adj_time.next_ == 0:
        ret = "[" + str(adj_time.prev_) + "대 운행중]" + \
              "\n" + str_time(adj_time.times_[0]) + "(" + str(time_diff(adj_time.times_[0], cur_time)) + "분전)" + \
              "\n" + str_time(adj_time.times_[1]) + "(" + str(time_diff(adj_time.times_[1], cur_time)) + "분전)" + \
              "\n\n" + \
              "[" + str(adj_time.next_) + "대 대기중]"
        return ret
    # case 6
    elif adj_time.prev_ == 2 and adj_time.next_ == 2:
        ret = "[" + str(adj_time.prev_) + "대 운행중]" + \
              "\n" + str_time(adj_time.times_[0]) + "(" + str(time_diff(adj_time.times_[0], cur_time)) + "분전)" + \
              "\n" + str_time(adj_time.times_[1]) + "(" + str(time_diff(adj_time.times_[1], cur_time)) + "분전)" + \
              "\n\n" + \
              "[" + str(adj_time.next_) + "대 대기중]" + \
              "\n" + str_time(adj_time.times_[2]) + "(" + str(time_diff(adj_time.times_[2], cur_time)) + "분후)" + \
              "\n" + str_time(adj_time.times_[3]) + "(" + str(time_diff(adj_time.times_[3], cur_time)) + "분후)"
        return ret


"""
인접 시간의 배열을 kakao json format으로 반환한다.
"""
def get_shuttle_answer():
    cur_time = datetime.now()
    # cur_time = get_datetime(time(16, 10))  # test code

    a = find_adjacent_times("A", cur_time)
    a_str = get_str_time_info(a, cur_time)
    answer = carousel_basic_card(
        a.line_name_ + "노선(순환)",
        a_str
    )

    b = find_adjacent_times("B", cur_time)
    b_str = get_str_time_info(b, cur_time)
    answer = insert_item(
        answer,
        b.line_name_ + "노선(순환)",
        b_str
    )

    cb_str = ""
    for t in LINE["CB"]:
        cb_str += str_time(t)
        cb_str += "\n"

    answer = insert_item(
        answer,
        "C노선(보운행)",
        cb_str
    )

    cd_str = ""
    for t in LINE["CD"]:
        cd_str += str_time(t)
        cd_str += "\n"

    answer = insert_item(
        answer,
        "C노선(대덕행)",
        cd_str
    )

    # 노선표 replies 추가
    answer = insert_multiple_reply(
        answer,
        [["A노선표", "A노선표"], ["B노선표", "B노선표"], ["C노선표", "C노선표"]]
    )
    return answer


"""
인자로 받은 노선에 대한 image kakao json format 반환
"""
def get_line_image(line):
    url = IMAGE_URL[line]
    answer = insert_image(url, line)
    answer = insert_multiple_reply(
        answer,
        [["A노선표", "A노선표"], ["B노선표", "B노선표"], ["C노선표", "C노선표"]]
    )
    return answer
