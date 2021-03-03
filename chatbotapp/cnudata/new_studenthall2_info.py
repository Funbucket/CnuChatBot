import requests
from bs4 import BeautifulSoup
from chatbotapp.kakaojsonformat.response import *

url = "http://cnuis.cnu.ac.kr/jsp/etc/toDayMenu.jsp"
req = requests.get(url)
req.raise_for_status()
soup = BeautifulSoup(req.content.decode('utf8', 'replace'), 'html.parser')


# 제2학생회관 , 3학생회관을 받아서 메뉴를 return 해주는 함수
def get_studenthall23_answer_info(name):
    # tr의 2번쨰는 학생식당을 뜻한다 tr의 3번째는 교직원식당 tr의 4번째는 학생식당(백반외 일품요리)
    student = soup.find("table", attrs={"class": "tab_color"}).find_all("tr", attrs={"align": "center"})[2]
    teacher = soup.find("table", attrs={"class": "tab_color"}).find_all("tr", attrs={"align": "center"})[3]
    student_special = soup.find("table", attrs={"class": "tab_color"}).find_all("tr", attrs={"align": "center"})[4]
    if name == "제2학생회관":
        student_menu = student.find_all("td")[2].get_text().strip()
        teacher_menu = teacher.find_all("td")[1].get_text().strip()
        student_special_menu = student_special.find_all("table" ,attrs={"width":"100%"})[0].find("td").get_text().strip()

    elif name == "제3학생회관":
        student_menu = student.find_all("td",attrs={"colspan":"2"})[1].get_text().strip()
        teacher_menu = teacher.find_all("table" ,attrs={"width":"100%"})[1].get_text().strip()
        student_special_menu = student_special.find_all("td")[4].get_text().strip()
    student_menu = ' '.join(student_menu.split())
    student_menu = student_menu.replace(" ", "\n")
    teacher_menu = ' '.join(teacher_menu.split())
    teacher_menu = teacher_menu.replace(" ", "\n")
    student_special_menu = ' '.join(student_special_menu.split())
    student_special_menu = student_special_menu.replace(" ", "\n")

    response_text = f"😚{name} 중식메뉴😚\n\n"
    response_text += "👉학생식당\n" + student_menu + "\n"
    response_text += "\n👉교직원식당\n" + teacher_menu + "\n"
    response_text += "\n👉학생식당(일품)\n" + student_special_menu

    answer = insert_text(response_text)
    reply = make_reply("다른 식당 메뉴보기", "학식")
    answer = insert_replies(answer, reply)

    return answer



