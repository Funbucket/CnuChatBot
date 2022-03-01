from chatbotapp.common.kakaojsonformat import *
from chatbotapp.models import ShuttleA, ShuttleB
from datetime import datetime, timedelta, time, date


"""
A : A노선 시간을 담은 배열
B : B노선 시간을 담은 배열 
"""
LINE = {
    "A": ShuttleA.objects.values_list('departureTime', flat=True).distinct(),
    "B": ShuttleB.objects.values_list('departureTime', flat=True).distinct()
}


"""
get_datetime
time object를 인자로 받아서 오늘의 datetime object 반환
"""
def get_datetime(time):
    return datetime.combine(date.today(), time)


"""
time object를 인자로 받으면 H:M 형식의 string object 반환
"""
def str_time(time):
    return time.strftime("%H:%M")


"""
find_adjacent_times
노선의 이름(A, B)과 현재 시간을 인자로 받아서 직전, 직후 인접 차량 시간을 배열로 반환한다.
"""
def find_adjacent_times(line_name, cur_time):
    line_times = LINE[line_name]
    last_index = len(line_times) - 1
    """
    case 1 : 운행종료, 00시 이후 첫차 출발 30 분전 
    case 2 : 운행종료, 마지막 차량 30분 이후 24시 이전
    case 3 : 직전 0개 직후 2개, (첫차 - 30분) 이후 첫차 직전
    case 4 : 직전 1개 직후 2개, 첫차 출발 직후 두번째차 출발 직전 
    case 5 : 직전 2개 직후 1개, 마지막 두번째 차 출발 직후 마지막차 출발 직전
    case 6 : 직적 2개 직후 0개, 마지막 출발 직후
    case 7 : 직전 2개 직후 2개, 반복문 
    """
    if get_datetime(time(0)) < cur_time < get_datetime(line_times[0]) - timedelta(minutes=30):
        return insert_card(
            line_name + "노선",
            "운행종료\n첫차시간은" + str_time(line_times[0])
        )
    elif get_datetime(line_times[last_index]) + timedelta(minutes=30) < cur_time < get_datetime(time(23, 59, 59)):
        return insert_card(
            line_name + "노선",
            "운행종료\n첫차시간은" + str_time(line_times[0])
        )
    elif get_datetime(line_times[0]) - timedelta(minutes=30) <= cur_time <= get_datetime(line_times[0]):
        return insert_card(
            line_name + "노선",
            str_time(line_times[0]) +
            "\n" + str_time(line_times[1])
        )
    elif get_datetime(line_times[0]) < cur_time <= get_datetime(line_times[1]):
        return insert_card(
            line_name + "노선",
            str_time(line_times[0]) +
            "\n" + str_time(line_times[1]) +
            "\n" + str_time(line_times[2])
        )
    elif get_datetime(line_times[last_index - 1]) < cur_time <= get_datetime(line_times[last_index]):
        return insert_card(
            line_name + "노선",
            str_time(line_times[last_index - 2]) +
            "\n" + str_time(line_times[last_index - 1]) +
            "\n" + str_time(line_times[last_index])
        )
    elif get_datetime(line_times[last_index]) < cur_time:
        return insert_card(
            line_name + "노선",
            str_time(line_times[last_index - 2]) +
            "\n" + str_time(line_times[last_index - 1])
        )
    else:
        for index, line_time in enumerate(line_times):
            if cur_time < get_datetime(line_time):
                return insert_card(
                    line_name + "노선",
                    str_time(line_times[index - 2]) +
                    "\n" + str_time(line_times[index - 1]) +
                    "\n" + str_time(line_times[index]) +
                    "\n" + str_time(line_times[index + 1])
                )


def get_shuttle_answer():
    cur_time = datetime.now()
    # cur_time = get_datetime(time(11, 21))
    aline_times = find_adjacent_times("A", cur_time)
    bline_times = find_adjacent_times("B", cur_time)

    return insert_card("shuttle", "shuttle info")


