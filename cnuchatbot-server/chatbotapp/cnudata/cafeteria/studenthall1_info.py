from chatbotapp.kakaojsonformat.response import *


def category():
    response_text = "제 1학생회관은 푸드코드입니다."
    answer = insert_text(response_text)
    reply = make_reply("운영시간", "운영시간")
    answer = insert_replies(answer, reply)
    reply = make_reply("라면&우동", "라면&우동")
    answer = insert_replies(answer, reply)
    reply = make_reply("간식", "간식")
    answer = insert_replies(answer, reply)
    reply = make_reply("양식", "양식")
    answer = insert_replies(answer, reply)
    reply = make_reply("스낵", "스낵")
    answer = insert_replies(answer, reply)
    reply = make_reply("한식", "한식")
    answer = insert_replies(answer, reply)
    reply = make_reply("일식", "일식")
    answer = insert_replies(answer, reply)
    reply = make_reply("중식", "중식")
    answer = insert_replies(answer, reply)
    return answer


def ramen():
    response_text = "[라면&우동]\n\n일반라면 : 2,000 \
                    \n떡만두라면 : 2,500 \
                    \n치즈라면 : 2,500 \
                    \n해장라면 : 3,000 \
                    \n가락우동 : 2,000 \
                    \n꼬치어묵우동 : 3,000 \
                    \n새우튀김우동 : 3,000 \
                    \n꼬치어묵 : 1,500 \
                    \n공기밥 : 500 "
    answer = insert_text(response_text)
    reply = make_reply("다른메뉴보기", "제1학생회관")
    answer = insert_replies(answer, reply)
    reply = make_reply("다른 식당 메뉴보기", "학식")
    answer = insert_replies(answer, reply)
    return answer


def gansik():
    response_text = "[간식]\n\n고기만두 : 1,500 \
                    \n김치만두 : 1,500 \
                    \n떡볶이 : 2,000 \
                    \n라볶이 : 3,000 \
                    \n치즈라볶이 : 3,500 \
                    \n야채김밥 : 1,800 \
                    \n소고기김밥 : 2,500 \
                    \n참치김밥 : 2,500 \
                    \n돈까스김밥 : 3,000 \
                    \n추억의도시락 : 3,000 "
    answer = insert_text(response_text)
    reply = make_reply("다른메뉴보기", "제1학생회관")
    answer = insert_replies(answer, reply)
    reply = make_reply("다른 식당 메뉴보기", "학식")
    answer = insert_replies(answer, reply)
    return answer


def america():
    response_text = "[양식]\n\n돈까스 : 4,000 \
                    \n치즈돈까스 : 4,500 \
                    \n치킨스테이크 : 4,000 \
                    \n새우튀김오므라이스 : 3,500 \
                    \n불닭오므라이스 : 3,500 \
                    \n토마토 해물 파스타 : 4,000 "

    answer = insert_text(response_text)
    reply = make_reply("다른메뉴보기", "제1학생회관")
    answer = insert_replies(answer, reply)
    reply = make_reply("다른 식당 메뉴보기", "학식")
    answer = insert_replies(answer, reply)
    return answer


def snack():
    response_text = "[스낵]\n\n별리달리 알밥 : 3,900 \
                    \n떡갈비추가 : 800 \
                    \n수제 떡갈비 버거(단품) : 3,500 \
                    \n수제 떡갈비 버거(세트) : 4,500 \
                    \n콜라/사이다 : 600 \
                    \n콜팝치킨 : 2,600 \
                    \n치킨커리 샌드위치 : 3,000 \
                    \n크리스피 치킨텐더(6PCS) : 3,700 \
                    \n크리스피 치킨텐더(세트) : 4,700 \
                    \n순살 후라이드 치킨(세트) : 8,400 \
                    \n순살 양념치킨(세트) : 9,400  \
                    \n순살 반반치킨(세트) : 9,400 "

    answer = insert_text(response_text)
    reply = make_reply("다른메뉴보기", "제1학생회관")
    answer = insert_replies(answer, reply)
    reply = make_reply("다른 식당 메뉴보기", "학식")
    answer = insert_replies(answer, reply)
    return answer


def korea():
    response_text = "[한식]\n\n바지락된장찌개 : 4,000 \
                    \n불고기비빔밥 : 4,700 \
                    \n해물순두부찌개 : 4,200 \
                    \n돈육김치찌개 : 4,200 \
                    \n부대찌개 : 5,000 \
                    \n뚝불고기 : 4,500 "

    answer = insert_text(response_text)
    reply = make_reply("다른메뉴보기", "제1학생회관")
    answer = insert_replies(answer, reply)
    reply = make_reply("다른 식당 메뉴보기", "학식")
    answer = insert_replies(answer, reply)
    return answer


def japan():
    response_text = "[일식]\n\n치킨마요덮밥(미니우동) : 3,900 \
                    \n제육덮밥(미니우동) : 4,200 \
                    \n카츠돈부리(미니우동) : 4,200 \
                    \n치킨돈부리(미니우동) : 4,200 \
                    \n김치카츠라이스(미니우동) : 4,500 \
                    \n카라아게카레(미니우동) : 4,700 \
                    \n카츠카레(미니우동) : 4,700 "

    answer = insert_text(response_text)
    reply = make_reply("다른메뉴보기", "제1학생회관")
    answer = insert_replies(answer, reply)
    reply = make_reply("다른 식당 메뉴보기", "학식")
    answer = insert_replies(answer, reply)
    return answer


def china():
    response_text = "[중식]\n\n옛날짜장 : 3,900 \
                    \n짜장곱배기 : 4,500 \
                    \n해물짬뽕 : 4,200 \
                    \n짬뽕곱배기 : 4,700 \
                    \n짬짜면 : 4,700 \
                    \n짬짜면곱배기 : 5,200 \
                    \n볶음밥 : 4,500 \
                    \n볶음밥곱배기+소스 : 5,000 \
                    \n탕수육 : 5,800 \
                    \n군만두 : 3,200 \
                    \n공기밥(중식) : 500 "
    
    answer = insert_text(response_text)
    reply = make_reply("다른메뉴보기", "제1학생회관")
    answer = insert_replies(answer, reply)
    reply = make_reply("다른 식당 메뉴보기", "학식")
    answer = insert_replies(answer, reply)
    return answer
