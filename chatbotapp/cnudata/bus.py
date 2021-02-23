from chatbotapp.kakaojsonformat.response import *

roots = ["A노선", "B노선"]
aroot_stations = ["정심화국제문화회관", "경상대학앞", "도서관 앞(농대방향)", "학생생활관3거리", "농업생명과학대학 앞", "동문주차장", "농업생명과학대학 앞", "도서관앞(도서관 삼거리 방향)",
            "예술대학앞", "음악2호관앞", "공동동물실험센터 입구(회차)", "체육관 입구", "서문(공동실험실습관앞)", "사회과학대학 입구(한누리회관뒤)", "산학연교육연구관앞"]


def get_root_answer():
    answer = insert_text("원하시는 노선을 선택해주세요.")

    for i in range(len(roots)):
        reply = make_reply(roots[i], roots[i])
        answer = insert_replies(answer, reply)

    return answer


def get_aroot_stations_answer():
    answer = insert_text("원하시는 정류장을 선택해주세요.")

    for i in range(len(aroot_stations)):
        reply = make_reply(aroot_stations[i], aroot_stations[i])
        answer = insert_replies(answer, reply)
    
    return answer
