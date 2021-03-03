from datetime import date, datetime, timedelta


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
def get_b3_who_how():
    now = datetime.now()
    # start_time = []
    # for i in range():
    #     start_time.append()
    start_time_1 = get_departure_time(8,50,0)
    start_time_2 = get_departure_time(9,20,0)
    start_time_3 = get_departure_time(9,50,0)
    start_time_4 = get_departure_time(10,20,0)
    start_time_5 = get_departure_time(11,20,0)
    start_time_6 = get_departure_time(13,20,0)
    start_time_7 = get_departure_time(13,50,0)
    start_time_8 = get_departure_time(14,50,0)
    start_time_9 = get_departure_time(15,20,0)
    start_time_10 = get_departure_time(15,50,0)
    start_time_11 = get_departure_time(16,20,0)
    start_time_12 = get_departure_time(16,50,0)
    start_time_13 = get_departure_time(17,20,0)
    start_time_14 = get_departure_time(17,55,0)
    # start_time_15 = get_departure_time(17,40,0)

    processed_start_time_1 = start_time_1 + timedelta(minutes=15,seconds=25)
    processed_start_time_2 = start_time_2 + timedelta(minutes=15,seconds=25)
    processed_start_time_3 = start_time_3 + timedelta(minutes=15,seconds=25)
    processed_start_time_4 = start_time_4 + timedelta(minutes=15,seconds=25)
    processed_start_time_5 = start_time_5 + timedelta(minutes=15,seconds=25)
    processed_start_time_6 = start_time_6 + timedelta(minutes=15,seconds=25)
    processed_start_time_7 = start_time_7 + timedelta(minutes=15,seconds=25)
    processed_start_time_8 = start_time_8 + timedelta(minutes=15,seconds=25)
    processed_start_time_9 = start_time_9 + timedelta(minutes=15,seconds=25)
    processed_start_time_10 = start_time_10 + timedelta(minutes=15,seconds=25)
    processed_start_time_11 = start_time_11 + timedelta(minutes=15,seconds=25)
    processed_start_time_12 = start_time_12 + timedelta(minutes=15,seconds=25)
    processed_start_time_13 = start_time_13 + timedelta(minutes=15,seconds=25)
    processed_start_time_14 = start_time_14 + timedelta(minutes=15,seconds=25)
    # processed_start_time_15 = start_time_15 + timedelta(minutes=15,seconds=25)
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


def get_b3_answer():
    who = get_b3_who_how()[0]
    how = get_b3_who_how()[1]
    # 현재 시간 now 가 배차가 있는 시간이라면 아래 실행
    if(type(how) == float):
        if 0<how<30:
            where_now = "정심화국제문화회관에서 출발"
        elif 30<=how<90:
            where_now = "사회과학대학입구(한누리회관 뒤)"
        elif 90<=how<130:
            where_now = "서문(공동실험실습관 앞)"
        elif 130<=how<230:
            where_now = "음악2호관 앞"
        elif 230<=how<290:
            where_now = "공동동물실험센터입구(회차)"
        elif 290<=how<360:
            where_now = "체육관입구"
        elif 360<=how<390:
            where_now = "예술대학 앞"
        elif 390<=how<430:
            where_now = "도서관 앞(대학본부옆농대방향)"
        elif 430<=how<510:
            where_now = "농업생명과학대학 앞(동문주자창 방향)"
        elif 510<=how<560:
            where_now = "동문주차장"
        elif 560<=how<630:
            where_now = "농업생명과학대학(학생생활관3거리방향)"
        elif 630<=how<820:
            where_now = "학생생활관3거리"
        elif 820<=how<860:
            where_now = "도서관 앞(도서관3거리방향)"
        elif 860<=how<900:
            where_now = "공과대학 앞"
        elif how>=925:
            where_now = "산학연구교육연구원 앞"

        who = who.strftime("%H:%M:%S")
        answer = "B-3호차\n[출발지]:정심화국제문화회관\n{}에 출발한 버스입니다\n[현재 예상위치]\n{}".format(who, where_now)
        return answer
    # 현재시간이 배차가 없는시간이라면 다음차 남은시간을 알려준다
    elif who == how:
        who = who.strftime("%H:%M:%S")
        answer = "B-3호차 운행종료 \n평일 첫차 {}".format(who)
        return answer
    else:
        who = who.strftime("%H:%M:%S")
        how = str(how)
        how = how[0:7]
        answer = "B-3호차현재운행차 없습니다. \n다음차 {} 까지 \n{}남았습니다.".format(who, how)
        return answer

