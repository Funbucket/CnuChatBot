from chatbotapp.kakaojsonformat.response import *

def category():
    response_text = "🍽제 1학생회관은 푸드코드로 운영되고 있습니다🍽\n\t🍴원하시는 식사 종류를 선택해주세요🍴"
    answer = insert_text(response_text)
    reply = make_reply("🍜라면", "라면")
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
    pass