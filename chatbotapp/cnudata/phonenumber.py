from chatbotapp.kakaojsonformat.response import *


def get_phone_number_answer():
    text = "필요할 때 꺼내보는 충남대학교 전화번호"
    text += "[학사지원과: 수업]\n042-821-5031\n042-821-5032\n042-821-5033\n"
    text += "[학사지원과: 학적]\n042-821-5042\n042-821-5043\n042-821-5044\n"
    text += "[중앙도서관]\n042-821-6023\n"
    text += "[학생과(장학)]\n042-821-5081\n"
    text += "[학생생활관]\n042-821-6181\n"
    text += "[재무과]\n042-821-5133\n"
    text += "[우체국]\n042-821-5185\n"
    text += "[민원서비스센터]\n042-821-5029\n"
    text += "[예비군 연대]\n042-821-6121\n"
    text += "[총무과(주차)]\n042-821-5113\n"
    text += "[입학본부]\n1644-8433\n"
    text += "[교내서점]\n042-821-5187\n"
    text += "[국제교류본부]\n042-821-5013\n"

    answer = insert_text(text)

    return answer

