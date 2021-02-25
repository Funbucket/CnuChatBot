from chatbotapp.kakaojsonformat.response import *
from datetime import datetime
from chatbotapp.info import bus_station_info as info

roots = ["A노선", "B노선"]
aroot_stations = ["정심화국제문화회관", "경상대학앞", "도서관 앞(농대방향)", "학생생활관3거리", "농업생명과학대학 앞(동문주자창 방향)", "동문주차장", "농업생명과학대학 앞",
                  "도서관앞(도서관 삼거리 방향)",
                  "예술대학앞", "음악2호관앞", "공동동물실험센터 입구(회차)", "체육관 입구", "서문(공동실험실습관앞)", "사회과학대학 입구(한누리회관뒤)", "산학연교육연구관앞"]
broot_stations = ["정심화국제문화회관", "사회과학대학입구(한누리회관뒤)", "서문(공동실험실습관앞)", "음악2호관앞", "공동동물실험센터입구(회차)", "체육관입구",
                  "예술대학앞", "도서관앞(대학본부옆농대방향)", "농업생명과학대학 앞", "동문주차장", "농업생명과학대학앞", "학생생활관3거리", "도서관앞(도서관삼거리 방향)",
                  "공과대학앞", "산학연교육연구관앞"]


def get_aline_arriving_time_answer(departure_hour, departure_minute):
    station_times = info.get_aline_times(departure_hour, departure_minute)
    # current_time = datetime.now()
    current_time = datetime(year=2021, month=2, day=26, hour=19, minute=00)
    for i in range(len(station_times)):
        # 17:55 이후 일 때
        if station_times[len(station_times) - 1] <= current_time:
            answer = insert_text("⏰운행이 종료되었습니다⏰")
            break
        # 11:30 ~ 13:00 일 때
        elif station_times[10] <= current_time <= station_times[11]:
            answer = insert_text("🍽휴식(중식)🍽🛸✈️🚀🕛")
            break
        elif current_time <= station_times[i]:
            difference_time = station_times[i] - current_time
            times = str(difference_time).split(":")
            print(station_times[i])
            answer_time = "🚌" + str(int(times[0]) * 60 + int(times[1])) + "분후 도착🚌 \n\n도착 시간은 노선별 운행표를 기반으로 제공하므로 미리 정류장에서 기다리는 것을 권장합니다😃"
            answer = insert_text(answer_time)
            break
    return answer


def get_bline_arriving_time_answer(departure_hour, departure_minute):
    station_times = info.get_bline_times(departure_hour, departure_minute)
    # current_time = datetime.now()
    current_time = datetime(year=2021, month=2, day=26, hour=12, minute=00)
    for i in range(len(station_times)):
        # 17:55 이후 일 때
        if station_times[len(station_times) - 1] <= current_time:
            answer = insert_text("⏰운행이 종료되었습니다⏰")
            break
        # 11:30 ~ 13:00 일 때
        elif station_times[16] <= current_time <= station_times[17]:
            answer = insert_text("🍽휴식(중식)🍽")
            break
        elif current_time <= station_times[i]:
            difference_time = station_times[i] - current_time
            times = str(difference_time).split(":")
            print(station_times[i])
            answer_time = "🚌" + str(int(times[0]) * 60 + int(times[1])) + "분후 도착🚌 \n\n도착 시간은 노선별 운행표를 기반으로 제공하므로 미리 정류장에서 기다리는 것을 권장합니다😃"
            answer = insert_text(answer_time)
            break
    return answer


def get_root_answer():
    answer = insert_text("😋 충남대학교 셔틀 정보 😋\n원하시는 노선을선택해주세요")
    for i in range(len(roots)):
        reply = make_reply(roots[i], roots[i])
        answer = insert_replies(answer, reply)
    return answer


def get_aroot_stations_answer():
    answer = insert_text("🚦원하시는 정류장을 선택해주세요🚦")

    for i in range(len(aroot_stations)):
        reply = make_reply("🌈" + aroot_stations[i], "A" + aroot_stations[i])
        answer = insert_replies(answer, reply)

    return answer


def get_broot_stations_answer():
    answer = insert_text("🚦원하시는 정류장을 선택해주세요🚦")

    for i in range(len(broot_stations)):
        reply = make_reply("🌈" + broot_stations[i], "B" + broot_stations[i])
        answer = insert_replies(answer, reply)

    return answer



