from chatbotapp.kakaojsonformat.response import *
from datetime import date, datetime, timedelta
roots = ["A노선", "B노선", "A노선표보기", "B노선표보기"]
aroot_stations = ["정심화국제문화회관", "경상대학앞", "도서관 앞(농대방향)", "학생생활관3거리", "농업생명과학대학 앞", "동문주차장", "농업생명과학대학 앞", "도서관앞(도서관 삼거리 방향)",
            "예술대학앞", "음악2호관앞", "공동동물실험센터 입구(회차)", "체육관 입구", "서문(공동실험실습관앞)", "사회과학대학 입구(한누리회관뒤)", "산학연교육연구관앞"]
broot_stations =["정심화국제문화회관", "사회과학대학입구(한누리회관뒤)", "서문(공동실험실습관앞)", "(임시정차)예술대학 앞", "음악2호관앞", "공동동물실험센터입구(회차)", "체육관입구", "예술대학앞", "도서관앞(대학본부옆농대방향)", "농업생명과학대학 앞", "동문주차장", "농업생명과학대학앞",  "학생생활관3거리", "도서관앞(도서관삼거리 방향)", "공과대학앞", "산학연교육연구관앞"]


year = date.today().year
month = date.today().month
day = date.today().day
arriving_time = datetime(year=year, month=month, day=day, hour=8, minute=30)

junsimhwa = []
am_departure_time = arriving_time
junsimhwa.append(am_departure_time)

for i in range(7):
    arriving_time += timedelta(minutes=15)
    str_time = arriving_time
    junsimhwa.append(str_time)

arriving_time += timedelta(minutes=45)
junsimhwa.append(arriving_time)

for i in range(2):
    arriving_time += timedelta(minutes=15)
    str_time = arriving_time
    junsimhwa.append(str_time)


arriving_time += timedelta(hours=1, minutes=30)
junsimhwa.append(arriving_time)

for i in range(3):
    arriving_time += timedelta(minutes=15)
    junsimhwa.append(arriving_time)

arriving_time += timedelta(minutes=45)
junsimhwa.append(arriving_time)

for i in range(12):
    arriving_time += timedelta(minutes=15)
    junsimhwa.append(arriving_time)

arriving_time += timedelta(minutes=25)
junsimhwa.append(arriving_time)
print(junsimhwa[1])

# print(junsimhwa[0])
# current_time = datetime.now()
current_time = datetime(year=year, month=month, day=day, hour=8, minute=55)
print(current_time)



for i in range(len(junsimhwa)):
    if junsimhwa[len(junsimhwa) - 1] <= current_time:
        print("운행이 종료되었습니다.")
        break
    elif junsimhwa[10] <= current_time <= junsimhwa[11]:
        print("휴식(중식)")
    elif current_time <= junsimhwa[i]:
        difference_time = junsimhwa[i] - current_time
        print(difference_time)
        answer = str(difference_time)
        break




def get_root_answer():
    answer = insert_text("원하시는 노선을 선택해주세요.")

    for i in range(len(roots)):

        reply = make_reply(roots[i], roots[i])
        answer = insert_replies(answer, reply)

    return answer



# aroot_image_url = "https://m.blog.naver.com/PostView.nhn?blogId=jhn5801&logNo=220670900645&proxyReferer=https:%2F%2Fwww.google.com%2F&view=img_1"


# def get_aroot_image(root):
#     answer = insert_image(aroot_image_url, root)
#     reply = make_reply("A노선보기", "A노선")
#     answer = insert_replies(answer, reply)
#
#     return answer


def get_broot_image():
    pass


def get_broot_stations_answer():
    answer = insert_text("원하시는 정류장을 선택해주세요.")

    for i in range(len(broot_stations)):
        reply = make_reply(broot_stations[i], broot_stations[i])
        answer = insert_replies(answer, reply)

    return answer


def get_aroot_stations_answer():
    answer = insert_text("원하시는 정류장을 선택해주세요.")

    for i in range(len(aroot_stations)):
        reply = make_reply(aroot_stations[i], aroot_stations[i])
        answer = insert_replies(answer, reply)

    return answer

