from datetime import datetime, timedelta
from chatbotapp.cnudata.shuttlebus.time import get_time


def get_departure_time_and_gap():
    now = datetime(2021, 6, 18, 9, 26)
    'now = datetime.now()'
    departure_times = []
    time = get_time(8, 45, 0)
    for i in range(4):
        departure_times.append(time)
        time += timedelta(minutes=30)
    time += timedelta(minutes=30)
    departure_times.append(time)
    time += timedelta(hours=2)
    departure_times.append(time)
    time += timedelta(minutes=30)
    departure_times.append(time)
    time += timedelta(hours=1)
    departure_times.append(time)
    for i in range(5):
        time += timedelta(minutes=30)
        departure_times.append(time)
    time += timedelta(minutes=40)
    departure_times.append(time)

    end_times = []
    for i in range(14):
        end_times.append(departure_times[i] + timedelta(minutes=20, seconds=00))

    if departure_times[0] <= now <= end_times[0]:
        return departure_times[0], (now - departure_times[0]).total_seconds()
    if end_times[0] < now <= departure_times[1]:
        return departure_times[1], departure_times[1] - now

    for i in range(1, 13):
        if departure_times[i] < now <= end_times[i]:
            return departure_times[i], (now - departure_times[i]).total_seconds()
        elif end_times[i] < now <= departure_times[i + 1]:
            return departure_times[i + 1], departure_times[i + 1] - now

    if departure_times[13] < now <= end_times[13]:
        return departure_times[13], (now - departure_times[13]).total_seconds()
    # 운행종료
    if end_times[13] < now or now.strftime("%H:%M:%S") < departure_times[0].strftime("%H:%M:%S"):
        return departure_times[0], departure_times[0]


def get_a2_answer():
    departure_time = get_departure_time_and_gap()[0]
    gap = get_departure_time_and_gap()[1]
    # 현재 시간 now 가 배차가 있는 시간이라면 아래 실행
    if type(gap) == float:
        departure_time = departure_time.strftime("%H:%M:%S")
        answer = "A-2호차 [운행중]\n[출발지] 정심화국제문화회관\n[출발시간] {}".format(departure_time)
        return answer

    elif departure_time == gap:
        departure_time = departure_time.strftime("%H:%M")
        answer = "A-2호차 [운행종료]\n[첫차] {}".format(departure_time)
        return answer
    else:
        departure_time = departure_time.strftime("%H:%M:%S")
        gap = str(gap)[0:7]
        # gap = how[0:7]
        answer = "A-2 [운행대기중]\n[남은시간] {}".format(gap)
        return answer


'''def get_a2_answer():
    departure_time = get_departure_time_and_gap()[0]
    gap = get_departure_time_and_gap()[1]
    # 현재 시간 now 가 배차가 있는 시간이라면 아래 실행
    where_now = ""
    if type(gap) == float:
        if 0 < gap < 30:
            where_now = "정심화국제문화회관에서 출발"
        elif 30 <= gap < 60:
            where_now = "경상대학 앞"
        elif 60 <= gap < 105:
            where_now = "도서관 앞(농대 방향)"
        elif 105 <= gap < 200:
            where_now = "학생생활관 3거리"
        elif 200 <= gap < 360:
            where_now = "농업생명과학대학 앞(동문주차장 방향)"
        elif 360 <= gap < 405:
            where_now = "동문 주차장"
        elif 405 <= gap < 495:
            where_now = "농업생명과학대학 앞(도서관 앞 방향)"
        elif 495 <= gap < 605:
            where_now = "도서관 앞(도서관 삼거리방향)"
        elif 605 <= gap < 650:
            where_now = "예술대학 앞"
        elif 650 <= gap < 715:
            where_now = "음악2호관 앞"
        elif 715 <= gap < 780:
            where_now = "동물실험센터입구(회차)"
        elif 780 <= gap < 870:
            where_now = "체육관 입구"
        elif 870 <= gap < 930:
            where_now = "서문(공동실험실습관 앞)"
        elif 930 <= gap < 970:
            where_now = "사회과학대학입구"
        elif gap >= 970:
            where_now = "산학연구교육연구원 앞"

        departure_time = departure_time.strftime("%H:%M:%S")
        answer = "A-2호차\n[출발지]:정심화국제문화회관\n{}에 출발한 버스입니다\n[현재 예상위치]\n{}".format(departure_time, where_now)
        return answer

    elif departure_time == gap:
        departure_time = departure_time.strftime("%H:%M")
        answer = "A-2호차 운행종료 \n평일 첫차 {}".format(departure_time)
        return answer
    else:
        departure_time = departure_time.strftime("%H:%M:%S")
        gap = str(gap)[0:7]
        # gap = how[0:7]
        answer = "A-2호차현재운행차 없습니다. \n다음차 {} 까지 \n{}남았습니다.".format(departure_time, gap)
        return answer
        '''

'''from datetime import date, datetime, timedelta


def get_departure_time(hour, minute, second):
    year = date.today().year
    month = date.today().month
    day = date.today().day
    departure_time = datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
    # departure_time = departure_time.strftime("%H:%m")
    return departure_time

def get_make_time(hour, minute, second):
    year = date.today().year
    month = date.today().month
    day = date.today().day
    departure_time = datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
    departure_time = departure_time.strftime("%M:%S")
    return departure_time


    # 현재 가장 최근 출발한 놈과 , 그 놈이 얼마만큼 시간경과했는지 알려줌
    # who 랑 how 16:07 분에 찍는다 그럼 who = 16:00  how = 00:07
def get_a2_who_how():
    # now = datetime.now()
    now = datetime(year=2021, month=3, day=6, hour=8, minute=47)
    start_time_1 = get_departure_time(8,45,0)
    start_time_2 = get_departure_time(9,15,0)
    start_time_3 = get_departure_time(9,45,0)
    start_time_4 = get_departure_time(10,15,0)
    start_time_5 = get_departure_time(11,15,0)
    start_time_6 = get_departure_time(13,15,0)
    start_time_7 = get_departure_time(13,45,0)
    start_time_8 = get_departure_time(14,45,0)
    start_time_9 = get_departure_time(15,15,0)
    start_time_10 = get_departure_time(15,45,0)
    start_time_11 = get_departure_time(16,15,0)
    start_time_12 = get_departure_time(16,45,0)
    start_time_13 = get_departure_time(17,15,0)
    start_time_14 = get_departure_time(17,55,0)

    processed_start_time_1 = start_time_1 + timedelta(minutes=16,seconds=20)
    processed_start_time_2 = start_time_2 + timedelta(minutes=16,seconds=20)
    processed_start_time_3 = start_time_3 + timedelta(minutes=16,seconds=20)
    processed_start_time_4 = start_time_4 + timedelta(minutes=16,seconds=20)
    processed_start_time_5 = start_time_5 + timedelta(minutes=16,seconds=20)
    processed_start_time_6 = start_time_6 + timedelta(minutes=16,seconds=20)
    processed_start_time_7 = start_time_7 + timedelta(minutes=16,seconds=20)
    processed_start_time_8 = start_time_8 + timedelta(minutes=16,seconds=20)
    processed_start_time_9 = start_time_9 + timedelta(minutes=16,seconds=20)
    processed_start_time_10 = start_time_10 + timedelta(minutes=16,seconds=20)
    processed_start_time_11 = start_time_11 + timedelta(minutes=16,seconds=20)
    processed_start_time_12 = start_time_12 + timedelta(minutes=16,seconds=20)
    processed_start_time_13 = start_time_13 + timedelta(minutes=16,seconds=20)
    processed_start_time_14 = start_time_14 + timedelta(minutes=16,seconds=20)
    # 각 if 앞에 걸리면 정상 출력 2번째 if 에 걸리면 미운행이므로 다음꺼 알려줌
    if start_time_1 <= now <= processed_start_time_1:
        return start_time_1 , (now - start_time_1).total_seconds()
    if processed_start_time_1 < now <= start_time_2:
        return start_time_2 , start_time_2 - now

    if start_time_2 < now <= processed_start_time_2:
        return start_time_2 , (now - start_time_2).total_seconds()
    if processed_start_time_2 < now <= start_time_3:
        return start_time_3 , start_time_3 - now

    if start_time_3 < now <= processed_start_time_3:
        return start_time_3 , (now - start_time_3).total_seconds()
    if processed_start_time_3 < now <= start_time_4:
        return start_time_4 , start_time_4 - now

    if start_time_4 < now <= processed_start_time_4:
        return start_time_4 , (now - start_time_4).total_seconds()
    if processed_start_time_4 < now <= start_time_5:
        return start_time_5 , start_time_5 - now

    if start_time_5 < now <= processed_start_time_5:
        return start_time_5 , (now - start_time_5).total_seconds()
    if processed_start_time_5 < now <= start_time_6:
        return start_time_6 , start_time_6 - now

    if start_time_6 < now <= processed_start_time_6:
        return start_time_6 , (now - start_time_6).total_seconds()
    if processed_start_time_6 < now <= start_time_7:
        return start_time_7 , start_time_7 - now

    if start_time_7 < now <= processed_start_time_7:
        return start_time_7 , (now - start_time_7).total_seconds()
    if processed_start_time_7 < now <= start_time_8:
        return start_time_8 , start_time_8 - now

    if start_time_8 < now <= processed_start_time_8:
        return start_time_8 , (now - start_time_8).total_seconds()
    if processed_start_time_8 < now <= start_time_9:
        return start_time_9 , start_time_9 - now

    if start_time_9 < now <= processed_start_time_9:
        return start_time_9 , (now - start_time_9).total_seconds()
    if processed_start_time_9 < now <= start_time_10:
        return start_time_10 , start_time_10 - now

    if start_time_10 < now <= processed_start_time_10:
        return start_time_10 , (now - start_time_10).total_seconds()
    if processed_start_time_10 < now <= start_time_11:
        return start_time_11 , start_time_11 - now

    if start_time_11 < now <= processed_start_time_11:
        return start_time_11 , (now - start_time_11).total_seconds()
    if processed_start_time_11 < now <= start_time_12:
        return start_time_12, start_time_12 - now

    if start_time_12 < now <= processed_start_time_12:
        return start_time_12 , (now - start_time_12).total_seconds()
    if processed_start_time_12 < now <= start_time_13:
        return start_time_13 , start_time_13 - now

    if start_time_13 < now <= processed_start_time_13:
        return start_time_13 , (now - start_time_13).total_seconds()
    if processed_start_time_13 < now <= start_time_14:
        return start_time_14 , start_time_14 - now



    if start_time_14 < now <= processed_start_time_14:
        return start_time_14 , (now - start_time_14).total_seconds()
    # 운행종료
    if processed_start_time_14 < now or now.strftime("%H:%M:%S") < start_time_1.strftime("%H:%M:%S"):
        return start_time_1, start_time_1
# how 는 얼마만큼 차이가나는 8시30열차가 출발하면 8시38분에찍은애는 how는 8분이야
# who 는 11시출발놈이다 11시30출발놈이다 넌 13:30출발놈이다
# 8시30 < who  8분 < how 8시38분에 찍는다면

def get_a2_answer():
    who = get_a2_who_how()[0]
    how = get_a2_who_how()[1]
    # 현재 시간 now 가 배차가 있는 시간이라면 아래 실행
    if(type(how) == float):
        if 0<how<30:
            where_now = "정심화국제문화회관에서 출발"
        elif 30<=how<60:
            where_now = " 경상대학 앞"
        elif 60<=how<105:
            where_now = "도서관 앞(농대 방향)"
        elif 105<=how<200:
            where_now = "학생생활관 3거리"
        elif 200<=how<360:
            where_now = "농업생명과학대학 앞(동문주차장 방향)"
        elif 360<=how<405:
            where_now = "동문 주차장"
        elif 405<=how<495:
            where_now = "농업생명과학대학 앞(도서관 앞 방향)"
        elif 495<=how<605:
            where_now = "도서관 앞(도서관 삼거리방향)"
        elif 605<=how<650:
            where_now = "예술대학 앞"
        elif 650<=how<715:
            where_now = "음악2호관 앞"
        elif 715<=how<780:
            where_now = "동물실험센터입구(회차)"
        elif 780<=how<870:
            where_now = "체육관 입구"
        elif 870<=how<930:
            where_now = "서문(공동실험실습관 앞)"
        elif 930<=how<970:
            where_now = "사회과학대학입구"
        elif how>=970:
            where_now = "산학연구교육연구원 앞"

        who = who.strftime("%H:%M:%S")
        answer = "A-2호차\n[출발지]:정심화국제문화회관\n{}에 출발한 버스입니다\n[현재 예상위치]\n{}".format(who,where_now)
        return answer
    #현재시간이 배차가 없는시간이라면 다음차 남은시간을 알려준다
    elif who == how:
        who = who.strftime("%H:%M")
        answer = "A-2호차 운행종료 \n평일 첫차 {}".format(who)
        return answer
    else:
        who = who.strftime("%H:%M:%S")
        how = str(how)
        how = how[0:7]
        answer = "A-2호차현재운행차 없습니다. \n다음차 {} 까지 \n{}남았습니다.".format(who,how)
        return answer'''
