from chatbotapp.kakaojsonformat.response import *

roots = ["A노선", "B노선", "A노선표보기", "B노선표보기"]
aroot_stations = ["정심화국제문화회관", "경상대학앞", "도서관 앞(농대방향)", "학생생활관3거리", "농업생명과학대학 앞", "동문주차장", "농업생명과학대학 앞", "도서관앞(도서관 삼거리 방향)",
            "예술대학앞", "음악2호관앞", "공동동물실험센터 입구(회차)", "체육관 입구", "서문(공동실험실습관앞)", "사회과학대학 입구(한누리회관뒤)", "산학연교육연구관앞"]
broot_stations =["정심화국제문화회관", "사회과학대학입구(한누리회관뒤)", "서문(공동실험실습관앞)", "(임시정차)예술대학 앞", "음악2호관앞", "공동동물실험센터입구(회차)", "체육관입구", "예술대학앞", "도서관앞(대학본부옆농대방향)", "농업생명과학대학 앞", "동문주차장", "농업생명과학대학앞",  "학생생활관3거리", "도서관앞(도서관삼거리 방향)", "공과대학앞", "산학연교육연구관앞"]


def get_root_answer():
    answer = insert_text("원하시는 노선을 선택해주세요.")

    for i in range(len(roots)):
        reply = make_reply(roots[i], roots[i])
        answer = insert_replies(answer, reply)

    return answer


aroot_image_url = "https://www.facebook.com/1638507039788764/photos/bc.Abq0WA0nlZ8S-MjE7X4Qfw69IwxyRN9YVL3oC8n8nj0ieH33mRksOTpiYvTDm-RaWKctLq6FnFk1l151wnhOxr3FAyZ_vjJ9y-XFl670e-Blzh6LE2C0Z0KNcexpsNWVKzWVW7o41BfZ8OxzM7YqpuUzReG3jMlxhwIoa0GELX1WmJWnk0u-Gyuh-1gBZmsBeXHj5ZqFdlC9Gu-Hia68ydb5/1762861957353271/?opaqueCursor=Abp9KMrGU16L9hXRjw9NsC5a39nkd6ToA7ePwblxfMHylq72X8GBsIwTdQLeQnzN2JGLc7H1a8LLiHLrlumzt_tBH5MX82CWOOpN0_EB8SDqdi15CY7Vkoi7ss9rI-ICo8CtCe6IIQoHxUsWrXTnKW1xoPIK1ExGeG1Gg4_rJaZmTYuzfRB2_FjYHgGNBfJHumspy8WNVGIE7MIIkYqtY3JedPUc8VeOQNm4R7o46auoI2xts8oe7QoNzdcO4wPVERd6UdQAggW0KvYKzEwj-1dbecB6zFjRXuDXzPCYjUpNEELttBvoMf43pS2XxE4risOxAHzuWW05UxfZ-LnmU6F66PUqEQTenmx5tWgrJgKpGbnCpBVYmwZ7CmCHzoxribx8S4WaHxOgi3n32b__EmVcNtbveC1me7Cax3h4f_6Vt5PQiyyTU-NhbFXfsYbB9B_djA4hp1CbmeZfA3vRdiVKIMJJdr8tKmudNrP7by_bUAvaWUD5_kE7a9qj35ucNleVZhpCT3W8uTD1-MvNU0n1dCfQ4j_Z_1945tWuigzcl2uIxO-eENwgJSaPVhNSNd2JoZvgUAko5L-L6chVQaM0PWVuLZK5XKrDQsscKW6hZA"


def get_aroot_image(root):
    answer = insert_image(aroot_image_url, root)
    reply = make_reply("A노선보기", "A노선")
    answer = insert_replies(answer, reply)

    return answer


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
