import requests
from bs4 import BeautifulSoup
from chatbotapp.common.kakaojsonformat import *
from enum import Enum
import re


class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
# today = dt.today()
# year = today.year
# month = today.month + 1
# day = 1


# def getDay_c():
#     daylist = ['월', '화', '수', '목', '금', '토', '일']
#     a = year
#     b = month
#     c = day
#     return daylist[datetime.date(a,b,c).weekday()]

# 4개의 td중에 0번째는 날짜 1번째는 아침 2번째는 점심 3번째는 저녁을 나타낸다
def when_numbering(when):
    if when == "breakfast":
        return 1
    elif when == "lunch":
        return 2
    elif when == "dinner":
        return 3


def english_to_korea_when(when):
    if when == "breakfast":
        answer = "아침"
    elif when == "lunch":
        answer = "점심"
    elif when == "dinner":
        answer = "저녁"
    return answer


def day_of_week_numbering(day_of_week):
    if day_of_week == "월":
        return 0
    elif day_of_week == "화":
        return 1
    elif day_of_week == "수":
        return 2
    elif day_of_week == "목":
        return 3
    elif day_of_week == "금":
        return 4
    elif day_of_week == "토":
        return 5
    elif day_of_week == "일":
        return 6


def dorm_menu(when, the_day_of_week_number):
    url = "https://dorm.cnu.ac.kr/html/kr/sub03/sub03_0304.html"
    req = requests.get(url)
    req.raise_for_status()
    soup = BeautifulSoup(req.content.decode('utf8', 'replace'), 'html.parser')
    dates = soup.find("table", attrs={"class": "default_view diet_table"}).find("tbody").find_all("tr")

    tr_tag = dates[the_day_of_week_number - 1]
    tds = tr_tag.find_all("td")
    index = when_numbering(when)        # index는 아침 점심 저녁을 의미한다.
    menu = tds[index].get_text()
    menu = ' '.join(menu.split())
    index = menu.find("메인A", 20)
    firstmainA = menu.find("메인A")
    secondMainA = menu.find("메인A",firstmainA+1)
    thirdMainA = menu.find("메인A",secondMainA+1) # after thirdMain that menu is english

    if (thirdMainA == -1):
        menu = menu[0:secondMainA]

    menu = menu[0:thirdMainA]       # 첨부터 영어 전까지 짜릅니다.
    menu = menu.replace("메", "\n--메")
    menu = menu.replace(" ", "\n")

    indexfirstopen = menu.find("A(")
    indexfirstclose = menu.find("l)")
    wantremove = menu[indexfirstopen+1:indexfirstclose+2]
    menu = menu.replace(wantremove, "--")

    indexsecondopen = menu.find("A(",firstmainA + 1)
    indexsecondclose = menu.find("l)",20)

    wantremove2 = menu[indexsecondopen+1:indexsecondclose+2]
    if(indexsecondopen != -1):
        menu = menu.replace(wantremove2, "--")

    day_of_week = ""
    if the_day_of_week_number == Weekday.MONDAY.value:
        day_of_week = "월"
    if the_day_of_week_number == Weekday.TUESDAY.value:
        day_of_week = "화"
    if the_day_of_week_number == Weekday.WEDNESDAY.value:
        day_of_week = "수"
    if the_day_of_week_number == Weekday.THURSDAY.value:
        day_of_week = "목"
    if the_day_of_week_number == Weekday.FRIDAY.value:
        day_of_week = "금"
    if the_day_of_week_number == Weekday.SATURDAY.value:
        day_of_week = "토"
    if the_day_of_week_number == Weekday.SUNDAY.value:
        day_of_week = "일"

    answer = "\n[{}]\n".format(english_to_korea_when(when)) + menu

    return answer
# print(dorm_menu("dinner",7))

# # when 은 아침점심저녁을 뜻한다 count 가 날짜를 뜻해준다
# def monday_dorm_menu(when , day_of_week ="월"):
#     dates = soup.find("table", attrs={"class": "default_view diet_table"}).find("tbody").find_all("tr")
#     # today_form = "{0}({1})".format(day, getDay_c())
#     # count = 0
#     # for date in dates:
#     #     if date.find("td").get_text().strip() == today_form:
#     #         break
#     #     count += 1
#     count = day_of_week_numbering(day_of_week)
#     # Ex count 가 4라면 7개의 tr 중에 0,1,2,3,(4),5,6  예라는 것이다
#     # 즉 현재기준 1(월) <== count 0 ,       3(수) <== count 2
#     # count 0 번째놈 크롤링
#     tr_tag = dates[count]
#     tds = tr_tag.find_all("td")
#     index = when_numbering(when)
#     menu = tds[index].get_text()
#     menu = ' '.join(menu.split())
#     menu = menu.replace(")", ")\n")
#     menu = menu.replace(" 메인", "\n메인")
#     menu = menu.replace(" ", "\n")
#     menu = menu.replace("메인", "-------------\n메인")
#     index = menu.find("메인A", 50)
#     menu = menu[0:index]
#     answer = "{}요일 {} 식단입니다\n".format(day_of_week, english_to_korea_when(when)) + menu
#
#     return answer

# def tuesday_dorm_menu(when , day_of_week ="화"):
#     dates = soup.find("table", attrs={"class": "default_view diet_table"}).find("tbody").find_all("tr")
#     # today_form = "{0}({1})".format(day, getDay_c())
#     # count = 0
#     # for date in dates:
#     #     if date.find("td").get_text().strip() == today_form:
#     #         break
#     #     count += 1
#     count = day_of_week_numbering(day_of_week)
#     # Ex count 가 4라면 7개의 tr 중에 0,1,2,3,(4),5,6  예라는 것이다
#     # 즉 현재기준 1(월) <== count 0 ,       3(수) <== count 2
#     # count 0 번째놈 크롤링
#     tr_tag = dates[count]
#     tds = tr_tag.find_all("td")
#     index = when_numbering(when)
#     menu = tds[index].get_text()
#     menu = ' '.join(menu.split())
#     menu = menu.replace(")", ")\n")
#     menu = menu.replace(" 메인", "\n메인")
#     menu = menu.replace(" ", "\n")
#     menu = menu.replace("메인", "-------------\n메인")
#     index = menu.find("메인A",50)
#     menu = menu[0:index]
#     answer = "{}요일 {} 식단입니다\n".format(day_of_week,english_to_korea_when(when)) + menu
#
#     return answer
#
#
# def wednesday_dorm_menu(when , day_of_week ="수"):
#     dates = soup.find("table", attrs={"class": "default_view diet_table"}).find("tbody").find_all("tr")
#     # today_form = "{0}({1})".format(day, getDay_c())
#     # count = 0
#     # for date in dates:
#     #     if date.find("td").get_text().strip() == today_form:
#     #         break
#     #     count += 1
#     count = day_of_week_numbering(day_of_week)
#     # Ex count 가 4라면 7개의 tr 중에 0,1,2,3,(4),5,6  예라는 것이다
#     # 즉 현재기준 1(월) <== count 0 ,       3(수) <== count 2
#     # count 0 번째놈 크롤링
#     tr_tag = dates[count]
#     tds = tr_tag.find_all("td")
#     index = when_numbering(when)
#     menu = tds[index].get_text()
#     menu = ' '.join(menu.split())
#     menu = menu.replace(")", ")\n")
#     menu = menu.replace(" 메인", "\n메인")
#     menu = menu.replace(" ", "\n")
#     menu = menu.replace("메인", "-------------\n메인")
#     index = menu.find("메인A", 50)
#     menu = menu[0:index]
#     answer = "{}요일 {} 식단입니다\n".format(day_of_week,english_to_korea_when(when)) + menu
#
#     return answer
#
#
# def thursday_dorm_menu(when , day_of_week ="목"):
#     dates = soup.find("table", attrs={"class": "default_view diet_table"}).find("tbody").find_all("tr")
#     # today_form = "{0}({1})".format(day, getDay_c())
#     # count = 0
#     # for date in dates:
#     #     if date.find("td").get_text().strip() == today_form:
#     #         break
#     #     count += 1
#     count = day_of_week_numbering(day_of_week)
#     # Ex count 가 4라면 7개의 tr 중에 0,1,2,3,(4),5,6  예라는 것이다
#     # 즉 현재기준 1(월) <== count 0 ,       3(수) <== count 2
#     # count 0 번째놈 크롤링
#     tr_tag = dates[count]
#     tds = tr_tag.find_all("td")
#     index = when_numbering(when)
#     menu = tds[index].get_text()
#     menu = ' '.join(menu.split())
#     menu = menu.replace(")", ")\n")
#     menu = menu.replace(" 메인", "\n메인")
#     menu = menu.replace(" ", "\n")
#     menu = menu.replace("메인", "-------------\n메인")
#     index = menu.find("메인A", 50)
#     menu = menu[0:index]
#     answer = "{}요일 {} 식단입니다\n".format(day_of_week, english_to_korea_when(when)) + menu
#
#     return answer
#
#
#
# def friday_dorm_menu(when , day_of_week ="금"):
#     dates = soup.find("table", attrs={"class": "default_view diet_table"}).find("tbody").find_all("tr")
#     # today_form = "{0}({1})".format(day, getDay_c())
#     # count = 0
#     # for date in dates:
#     #     if date.find("td").get_text().strip() == today_form:
#     #         break
#     #     count += 1
#     count = day_of_week_numbering(day_of_week)
#     # Ex count 가 4라면 7개의 tr 중에 0,1,2,3,(4),5,6  예라는 것이다
#     # 즉 현재기준 1(월) <== count 0 ,       3(수) <== count 2
#     # count 0 번째놈 크롤링
#     tr_tag = dates[count]
#     tds = tr_tag.find_all("td")
#     index = when_numbering(when)
#     menu = tds[index].get_text()
#     menu = ' '.join(menu.split())
#     menu = menu.replace(")", ")\n")
#     menu = menu.replace(" 메인", "\n메인")
#     menu = menu.replace(" ", "\n")
#     menu = menu.replace("메인", "-------------\n메인")
#     index = menu.find("메인A", 50)
#     menu = menu[0:index]
#     answer = "{}요일 {} 식단입니다\n".format(day_of_week, english_to_korea_when(when)) + menu
#
#     return answer
#
#
# def saturday_dorm_menu(when , day_of_week ="토"):
#     dates = soup.find("table", attrs={"class": "default_view diet_table"}).find("tbody").find_all("tr")
#     # today_form = "{0}({1})".format(day, getDay_c())
#     # count = 0
#     # for date in dates:
#     #     if date.find("td").get_text().strip() == today_form:
#     #         break
#     #     count += 1
#     count = day_of_week_numbering(day_of_week)
#     # Ex count 가 4라면 7개의 tr 중에 0,1,2,3,(4),5,6  예라는 것이다
#     # 즉 현재기준 1(월) <== count 0 ,       3(수) <== count 2
#     # count 0 번째놈 크롤링
#     tr_tag = dates[count]
#     tds = tr_tag.find_all("td")
#     index = when_numbering(when)
#     menu = tds[index].get_text()
#     menu = ' '.join(menu.split())
#     menu = menu.replace(")", ")\n")
#     menu = menu.replace(" 메인", "\n메인")
#     menu = menu.replace(" ", "\n")
#     menu = menu.replace("메인", "-------------\n메인")
#     index = menu.find("메인A", 50)
#     menu = menu[0:index]
#     answer = "{}요일 {} 식단입니다\n".format(day_of_week,english_to_korea_when(when)) + menu
#
#     return answer
#
# def sunday_dorm_menu(when , day_of_week ="일"):
#     dates = soup.find("table", attrs={"class": "default_view diet_table"}).find("tbody").find_all("tr")
#     # today_form = "{0}({1})".format(day, getDay_c())
#     # count = 0
#     # for date in dates:
#     #     if date.find("td").get_text().strip() == today_form:
#     #         break
#     #     count += 1
#     count = day_of_week_numbering(day_of_week)
#     # Ex count 가 4라면 7개의 tr 중에 0,1,2,3,(4),5,6  예라는 것이다
#     # 즉 현재기준 1(월) <== count 0 ,       3(수) <== count 2
#     # count 0 번째놈 크롤링
#     tr_tag = dates[count]
#     tds = tr_tag.find_all("td")
#     index = when_numbering(when)
#     menu = tds[index].get_text()
#     menu = ' '.join(menu.split())
#     menu = menu.replace(")", ")\n")
#     menu = menu.replace(" 메인", "\n메인")
#     menu = menu.replace(" ", "\n")
#     menu = menu.replace("메인", "-------------\n메인")
#     index = menu.find("메인A", 50)
#     menu = menu[0:index]
#     answer = "{}요일 {} 식단입니다\n".format(day_of_week,english_to_korea_when(when)) + menu
#
#     return answer

# dorm_menu(2, )


def dorm_time():
    url = "https://dorm.cnu.ac.kr/html/kr/sub03/sub03_0304.html"
    req = requests.get(url)
    req.raise_for_status()
    date_soup = BeautifulSoup(req.content.decode('utf8', 'replace'), 'html.parser')
    term = date_soup.find("div", attrs={"class": "diet_table_top"}).get_text().strip()
    text = f"[{term}]\n\n[아침]\n07:30 ~ 09:00\n\n[점심]\n11:30 ~ 13:30\n\n[저녁]\n17:00 ~ 19:30\n(주말 및 공휴일은 17:30 ~ 19:00)\n"
    answer = insert_text(text)
    reply = make_reply("오늘", "오늘기숙사식당")
    answer = insert_replies(answer, reply)
    reply = make_reply("월", "월요일기숙사식당")
    answer = insert_replies(answer, reply)
    reply = make_reply("화", "화요일기숙사식당")
    answer = insert_replies(answer, reply)
    reply = make_reply("수", "수요일기숙사식당")
    answer = insert_replies(answer, reply)
    reply = make_reply("목", "목요일기숙사식당")
    answer = insert_replies(answer, reply)
    reply = make_reply("금", "금요일기숙사식당")
    answer = insert_replies(answer, reply)
    reply = make_reply("토", "토요일기숙사식당")
    answer = insert_replies(answer, reply)
    reply = make_reply("일", "일요일기숙사식당")
    answer = insert_replies(answer, reply)

    return answer

def day_of_week(the_day_of_week):
    text = "⏱️시간을 골라주세요⏱️"
    answer = insert_text(text)

    if Weekday.MONDAY.name == the_day_of_week:

        reply = make_reply("🌅아침", "월[아침]")
        answer = insert_replies(answer, reply)
        reply = make_reply("☀️점심", "월[점심]")
        answer = insert_replies(answer, reply)
        reply = make_reply("🌙저녁", "월[저녁]")
        answer = insert_replies(answer, reply)

    elif Weekday.TUESDAY.name == the_day_of_week:

        reply = make_reply("🌅아침", "화[아침]")
        answer = insert_replies(answer, reply)
        reply = make_reply("☀️점심", "화[점심]")
        answer = insert_replies(answer, reply)
        reply = make_reply("🌙저녁", "화[저녁]")
        answer = insert_replies(answer, reply)

    elif Weekday.WEDNESDAY.name == the_day_of_week:

        reply = make_reply("🌅아침", "수[아침]")
        answer = insert_replies(answer, reply)
        reply = make_reply("☀️점심", "수[점심]")
        answer = insert_replies(answer, reply)
        reply = make_reply("🌙저녁", "수[저녁]")
        answer = insert_replies(answer, reply)

    elif Weekday.THURSDAY.name == the_day_of_week:

        reply = make_reply("🌅아침", "목[아침]")
        answer = insert_replies(answer, reply)
        reply = make_reply("☀️점심", "목[점심]")
        answer = insert_replies(answer, reply)
        reply = make_reply("🌙저녁", "목[저녁]")
        answer = insert_replies(answer, reply)

    elif Weekday.FRIDAY.name == the_day_of_week:

        reply = make_reply("🌅아침", "금[아침]")
        answer = insert_replies(answer, reply)
        reply = make_reply("☀️점심", "금[점심]")
        answer = insert_replies(answer, reply)
        reply = make_reply("🌙저녁", "금[저녁]")
        answer = insert_replies(answer, reply)

    elif Weekday.SATURDAY.name == the_day_of_week:

        reply = make_reply("🌅아침", "토[아침]")
        answer = insert_replies(answer, reply)
        reply = make_reply("☀️점심", "토[점심]")
        answer = insert_replies(answer, reply)
        reply = make_reply("🌙저녁", "토[저녁]")
        answer = insert_replies(answer, reply)

    elif Weekday.SUNDAY.name == the_day_of_week:

        reply = make_reply("🌅아침", "일[아침]")
        answer = insert_replies(answer, reply)
        reply = make_reply("☀️점심", "일[점심]")
        answer = insert_replies(answer, reply)
        reply = make_reply("🌙저녁", "일[저녁]")
        answer = insert_replies(answer, reply)

    return answer


# def monday():
#     text = "⏱️시간을 골라주세요⏱️"
#     answer = insert_text(text)
#     reply = make_reply("🌅아침", "월[아침]")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("☀️점심", "월[점심]")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("🌙저녁", "월[저녁]")
#     answer = insert_replies(answer, reply)
#
#     return answer
#
# def tuesday():
#     text = "⏱️시간을 골라주세요⏱️"
#     answer = insert_text(text)
#     reply = make_reply("🌅아침", "화[아침]")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("☀️점심", "화[점심]")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("🌙저녁", "화[저녁]")
#     answer = insert_replies(answer, reply)
#
#     return answer
#
# def wednesday():
#     text = "⏱️시간을 골라주세요⏱️"
#     answer = insert_text(text)
#     reply = make_reply("🌅아침", "수[아침]")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("☀️점심", "수[점심]")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("🌙저녁", "수[저녁]")
#     answer = insert_replies(answer, reply)
#
#     return answer
#
# def thursday():
#     text = "⏱️시간을 골라주세요⏱️"
#     answer = insert_text(text)
#     reply = make_reply("🌅아침", "목[아침]")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("☀️점심", "목[점심]")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("🌙저녁", "목[저녁]")
#     answer = insert_replies(answer, reply)
#
#     return answer
#
# def friday():
#     text = "⏱️시간을 골라주세요⏱️"
#     answer = insert_text(text)
#     reply = make_reply("🌅아침", "금[아침]")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("☀️점심", "금[점심]")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("🌙저녁", "금[저녁]")
#     answer = insert_replies(answer, reply)
#
#     return answer
#
# def saturday():
#     text = "⏱️시간을 골라주세요⏱️"
#     answer = insert_text(text)
#     reply = make_reply("🌅아침", "토[아침]")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("☀️점심", "토[점심]")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("🌙저녁", "토[저녁]")
#     answer = insert_replies(answer, reply)
#
#     return answer
#
# def sunday():
#     text = "⏱️시간을 골라주세요⏱️"
#     answer = insert_text(text)
#     reply = make_reply("🌅아침", "일[아침]")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("☀️점심", "일[점심]")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("🌙저녁", "일[저녁]")
#     answer = insert_replies(answer, reply)
#
#     return answer
#
