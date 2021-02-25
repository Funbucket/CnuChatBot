# 기타에 대한 정보
from chatbotapp.kakaojsonformat.response import *

def get_error_answer():
    openurl = "https://open.kakao.com/o/sm0C6bZc"
    answer = insert_text("⁉️오류제보 / 기능 건의 ⁉️\n {}\n 링크를 클릭후 \n 편하게 채팅해주세요\n 여러분들의 오류제보가 \n백마봇을 더 성장시킵니다".format(openurl))
    reply = make_reply("🏡홈으로", "홈")
    answer = insert_replies(answer, reply)
    reply = make_reply("ℹ️개발자 정보", "ℹ️개발자 정보")
    answer = insert_replies(answer, reply)
    return answer

def get_information_answer():
    our_information = "😎\t\t충남대백마봇 공동개발자\t\t😎\n🥳조해창 : ouchc@icloud.com\n🤩박찬혁 : chanhyuk-tech@kakao.com\n"
    answer = insert_text(our_information)
    reply = make_reply("🏡홈으로", "홈")
    answer = insert_replies(answer, reply)
    reply = make_reply("📬오류 제보 / 기능 건의📬", "📬오류 제보 / 기능 건의📬")
    answer = insert_replies(answer, reply)
    return answer