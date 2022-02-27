import requests
from bs4 import BeautifulSoup
from chatbotapp.common.kakaojsonformat import *
from chatbotapp.cnudata.is_vacation import get_vacation
# 제2학생회관 , 3학생회관을 받아서 메뉴를 return 해주는 함수


def get_studenthall23_answer_info(name):
    try:
        url = "http://cnuis.cnu.ac.kr/jsp/etc/toDayMenu.jsp"
        req = requests.get(url)
        req.raise_for_status()
        soup = BeautifulSoup(req.content.decode('utf8', 'replace'), 'html.parser')
    except:
        text = "현재 학교 홈페이지가 원활하지 않습니다\n잠시후 다시 이용해주세요 😚"
        answer = insert_text(text)
        reply = make_reply("다른 식당 메뉴보기", "학식")
        answer = insert_replies(answer, reply)
        return answer

    #주말이라면
    if get_vacation():
        response_text = f"주말 및 공휴일에는 운영하지 않습니다"
        answer = insert_text(response_text)
        reply = make_reply("다른 식당 메뉴보기", "학식")
        answer = insert_replies(answer, reply)
        return answer


    #평일이라면
    else:
        # tr의 2번쨰는 학생식당을 뜻한다 tr의 3번째는 교직원식당 tr의 4번째는 학생식당(백반외 일품요리)
        student = soup.find("table", attrs={"class": "tab_color"}).find_all("tr", attrs={"align": "center"})[2]
        teacher = soup.find("table", attrs={"class": "tab_color"}).find_all("tr", attrs={"align": "center"})[3]
        student_special = soup.find("table", attrs={"class": "tab_color"}).find_all("tr", attrs={"align": "center"})[4]
        if name == "제2학생회관":
            student_menu = student.find_all("td", attrs={"height":"20"})[2].get_text().strip()
            student_price = student.find_all("td", attrs={"height":"20"})[3].get_text().strip()
            student_price = "[" + student_price + "원]\n"
            teacher_menu = teacher.find_all("td", attrs={"height":"20"})[1].get_text().strip()
            teacher_price = teacher.find_all("td", attrs={"height": "20"})[2].get_text().strip()
            teacher_price = "[" + teacher_price + "원]\n"
            student_special_menu = student_special.find_all("table", attrs={"width":"100%"})[0].find_all("td")[0].get_text().strip()
            student_special_price = "[" + student_special.find_all("table", attrs={"width":"100%"})[0].find_all("td")[1].get_text().strip() + "원]\n"

        elif name == "제3학생회관":
            student_menu = "[" + student.find_all("td",attrs={"colspan":"2"})[1].get_text().strip() +"]"
            student_price = ""
            teacher_menu = teacher.find_all("table" ,attrs={"width":"100%"})[1].get_text().strip()
            teacher_price = "[" + teacher.find_all("td", attrs={"height": "20"})[4].get_text().strip() + "원]"
            student_special_menu = "[" + student_special.find_all("td", attrs={"colspan": "2"})[1].get_text().strip() + "]"
            student_special_price = ""

        student_menu = ' '.join(student_menu.split()).replace(" ", "\n")
        teacher_menu = ' '.join(teacher_menu.split()).replace(" ", "\n")
        student_special_menu = ' '.join(student_special_menu.split()).replace(" ", "\n")

        # response_text = f"{name} 중식메뉴\n\n"
        response_text = "[학생식당]\n\n" + student_menu + "\n"
        response_text += "\n[교직원식당]\n" + teacher_menu + "\n"
        response_text += "\n[학생식당(일품)]\n" + student_special_menu
        # print(response_text)
        answer = insert_text(response_text)
        reply = make_reply("다른 식당 메뉴보기", "학식")
        answer = insert_replies(answer, reply)

        return answer



