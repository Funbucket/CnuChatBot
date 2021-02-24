from chatbotapp.kakaojsonformat.response import *

def category():
    response_text = "😋제 1학생회관을 선택하셨습니다😋 \n\t\t\t제 1학생회관은\n 푸드코드로 운영되고 있습니다🍽\n\t🍴원하시는 식사 종류를🍴\n\t\t\t 선택해주세요"
    answer = insert_text(response_text)
    reply = make_reply("🍜라면&우동", "라면&우동")
    answer = insert_replies(answer, reply)
    reply = make_reply("🍙간식", "간식")
    answer = insert_replies(answer, reply)
    reply = make_reply("🥩양식", "양식")
    answer = insert_replies(answer, reply)
    reply = make_reply("🥠스낵", "스낵")
    answer = insert_replies(answer, reply)
    reply = make_reply("🥘한식", "한식")
    answer = insert_replies(answer, reply)
    reply = make_reply("🍛일식", "일식")
    answer = insert_replies(answer, reply)
    reply = make_reply("🥟중식", "중식")
    answer = insert_replies(answer, reply)
    return answer

def ramen():
    response_text = "😋   라면&우동 메뉴를 선택하셨습니다   😋\n\t\t 일반라면 : 2,000 \
                    \n\t\t 떡만두라면 : 2,500 \
                    \n\t\t 치즈라면 : 2,500 \
                    \n\t\t 해장라면 : 3,000 \
                    \n\t\t 가락우동 : 2,000 \
                    \n\t\t 꼬치어묵우동 : 3,000 \
                    \n\t\t 새우튀김우동 : 3,000 \
                    \n\t\t 꼬치어묵 : 1,500 \
                    \n\t\t 공기밥 : 500 "
    answer = insert_text(response_text)
    return answer

