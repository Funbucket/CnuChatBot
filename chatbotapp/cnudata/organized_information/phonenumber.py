from chatbotapp.kakaojsonformat.response import *


def get_phone_number_answer():
    text = "\t☎️충남대학교 전화번호☎️\t\n\n"
    text += "[학사지원과: 수업]\n042-821-5031\n042-821-5032\n042-821-5033\n"
    text += "\n[학사지원과: 학적]\n042-821-5042\n042-821-5043\n042-821-5044\n"
    text += "\n[중앙도서관]\n042-821-6023\n"
    text += "\n[학생과(장학)]\n042-821-5081\n"
    text += "\n[학생생활관]\n042-821-6181\n"
    text += "\n[재무과]\n042-821-5133\n"
    text += "\n[우체국]\n042-821-5185\n"
    text += "\n[민원서비스센터]\n042-821-5029\n"
    text += "\n[예비군 연대]\n042-821-6121\n"
    text += "\n[총무과(주차)]\n042-821-5113\n"
    text += "\n[입학본부]\n1644-8433\n"
    text += "\n[교내서점]\n042-821-5187\n"
    text += "\n[국제교류본부]\n042-821-5013"

    answer = insert_text(text)

    return answer

