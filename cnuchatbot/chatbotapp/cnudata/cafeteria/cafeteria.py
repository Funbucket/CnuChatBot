from chatbotapp.cnudata.cafeteria.studenthall1_info import *
from chatbotapp.cnudata.cafeteria.food_court_time import *
from chatbotapp.cnudata.cafeteria.dorm_info import *
from chatbotapp.cnudata.cafeteria.new_studenthall2_info import *
from chatbotapp.common.variables.cafeteria import *
from chatbotapp.common.functions import *
from GrabzIt import GrabzItImageOptions
from GrabzIt import GrabzItClient
from datetime import datetime
import requests
import schedule


def get_entire_cafeteria_info():
    response_text = "충남대학교 학식 정보"
    answer = insert_text(response_text)
    answer = insert_multiple_reply(answer, cafeteriaNormalReplies)
    return answer


def get_studenthall1_answer():
    answer = insert_image(studenthall1Image_BASE_URL, "img")
    answer = insert_multiple_reply(answer, cafeteriaNormalReplies)
    return answer


def get_variousCafeteria_info():
    text = "보고 싶은 식당을 선택해주세요"
    answer = insert_text(text)
    answer = insert_multiple_reply(answer, [["학생", "학생"], ["교직원", "교직원"]])
    return answer


# http://3.38.250.164/cnuchatbot/media/savedImage/123.png/
def get_variousCafeteria_answer(person):
    # default 교직원
    personCategory = "CCS01.10"

    if person == "학생":
        personCategory = "CCS01.20"

    answer = make_card(
        mealCategoryKoreans[0],
        "",
        "http://3.38.250.164/cnuchatbot/media/savedImage/{}-{}.png".format(
            personCategory, mealCategory[0]
        ),
    )

    for index in range(1, 5):
        insert_card(
            answer,
            mealCategoryKoreans[index],
            "",
            "http://3.38.250.164/cnuchatbot/media/savedImage/{}-{}.png".format(
                personCategory, mealCategory[index]
            ),
        )

    return answer


def get_variousCafeteria_images():
    # jsp 사진 보내주는 로직
    grabzIt = GrabzItClient.GrabzItClient(
        "ZjQyYTIyZTgyZWE0NGZjMDk3NDdlZTQ0ZWQyNTdkN2I=",
        "P2cOP3Q/AD8/FQ8MP3c/P3MDH0U5Dgw/Px0/OD8/Txs=",
    )
    options = GrabzItImageOptions.GrabzItImageOptions()
    options.browserHeight = -1

    options.format = "png"
    options.width = -1
    options.height = -1
 
    for person in personCategory:
        for meal in mealCategory:
            data = {"cafe_div_cd": person, "food_div_cd": meal, "langType": "1"}
            r = requests.post(
                variousCafeteria_BASE_URL,
                data=data,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
            grabzIt.HTMLToImage(r.text, options)
            # Then call the Save or SaveTo method
            grabzIt.SaveTo(
                "cnuchatbot/media/savedImage/{0}-{1}.png".format(person, meal)
            )
    return insert_text("sad")

# get_variousCafeteria_images()
# 매주 월요일에 동작
schedule.every().monday.do(get_variousCafeteria_images)


def get_studenthall23_answer(name):
    answer = get_studenthall23_answer_info(name)
    return answer


def get_entire_time():
    answer = entire_time()
    return answer


def day_of_week_dorm(the_day_of_week_number):

    if Weekday.MONDAY.value == the_day_of_week_number:
        answer = day_of_week("MONDAY")
    if Weekday.TUESDAY.value == the_day_of_week_number:
        answer = day_of_week("TUESDAY")
    if Weekday.WEDNESDAY.value == the_day_of_week_number:
        answer = day_of_week("WEDNESDAY")
    if Weekday.THURSDAY.value == the_day_of_week_number:
        answer = day_of_week("THURSDAY")
    if Weekday.FRIDAY.value == the_day_of_week_number:
        answer = day_of_week("FRIDAY")
    if Weekday.SATURDAY.value == the_day_of_week_number:
        answer = day_of_week("SATURDAY")
    if Weekday.SUNDAY.value == the_day_of_week_number:
        answer = day_of_week("SUNDAY")

    return answer


# def get_monday_breakfast_menu():
#     text = monday_dorm_menu("breakfast")
#     answer = insert_text(text)
#     reply = make_reply("다른식당보기", "학식")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("다른요일보기", "기숙사식당")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("다른시간보기", "월요일기숙사식당")
#     answer = insert_replies(answer, reply)
#
#     return answer
#
# def get_monday_lunch_menu():
#     text = monday_dorm_menu("lunch")
#     answer = insert_text(text)
#     reply = make_reply("다른식당보기", "학식")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("다른요일보기", "기숙사식당")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("다른시간보기", "월요일기숙사식당")
#     answer = insert_replies(answer, reply)
#
#     return answer
#
# def get_monday_dinner_menu():
#     text = monday_dorm_menu("dinner")
#     answer = insert_text(text)
#     reply = make_reply("다른식당보기", "학식")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("다른요일보기", "기숙사식당")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("다른시간보기", "월요일기숙사식당")
#     answer = insert_replies(answer, reply)
#
#     return answer


def get_entire_menu(when, the_day_of_week_number):
    # if Weekday.MONDAY.value == the_day_of_week_number:
    #     reply = make_reply("다른시간보기", "월요일기숙사식당")
    # if Weekday.TUESDAY.value == the_day_of_week_number:
    #     reply = make_reply("다른시간보기", "화요일기숙사식당")
    # if Weekday.WEDNESDAY.value == the_day_of_week_number:
    #     reply = make_reply("다른시간보기", "수요일기숙사식당")
    # if Weekday.THURSDAY.value == the_day_of_week_number:
    #     reply = make_reply("다른시간보기", "목요일기숙사식당")
    # if Weekday.FRIDAY.value == the_day_of_week_number:
    #     reply = make_reply("다른시간보기", "금요일기숙사식당")
    # if Weekday.SATURDAY.value == the_day_of_week_number:
    #     reply = make_reply("다른시간보기", "토요일기숙사식당")
    # if Weekday.SUNDAY.value == the_day_of_week_number:
    #     reply = make_reply("다른시간보기", "일요일기숙사식당")

    # text = dorm_menu(when, the_day_of_week_number) 원래 이거였는데 , 3가지 다 한꺼번에 나오도록
    text = dorm_menu("breakfast", the_day_of_week_number)
    text += "\n"
    text += dorm_menu("lunch", the_day_of_week_number)
    text += "\n"

    text += dorm_menu("dinner", the_day_of_week_number)

    answer = insert_text(text)
    # answer = insert_replies(answer,reply)
    reply = make_reply("다른식당보기", "학식")
    answer = insert_replies(answer, reply)
    reply = make_reply("다른요일보기", "기숙사식당")
    answer = insert_replies(answer, reply)
    return answer


# print(get_entire_menu("breakfast",1))


#
# def get_monday_menu(when):
#     text = monday_dorm_menu(when)
#     answer = insert_text(text)
#     reply = make_reply("다른시간보기", "월요일기숙사식당")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("다른식당보기", "학식")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("다른요일보기", "기숙사식당")
#     answer = insert_replies(answer, reply)
#
#
#     return answer
#
# def get_tuesday_menu(when):
#     text = tuesday_dorm_menu(when)
#     answer = insert_text(text)
#     reply = make_reply("다른식당보기", "학식")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("다른요일보기", "기숙사식당")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("다른시간보기", "화요일기숙사식당")
#     answer = insert_replies(answer, reply)
#     return answer
# # def get_tuesday_breakfast_menu():
# #     text = tuesday_dorm_menu("breakfast")
# #     answer = insert_text(text)
# #     reply = make_reply("다른식당보기", "학식")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른요일보기", "기숙사식당")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른시간보기", "화요일기숙사식당")
# #     answer = insert_replies(answer, reply)
# #
# #     return answer
# #
# # def get_tuesday_lunch_menu():
# #     text = tuesday_dorm_menu("lunch")
# #     answer = insert_text(text)
# #     reply = make_reply("다른식당보기", "학식")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른요일보기", "기숙사식당")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른시간보기", "화요일기숙사식당")
# #     answer = insert_replies(answer, reply)
# #
# #     return answer
# #
# # def get_tuesday_dinner_menu():
# #     text = tuesday_dorm_menu("dinner")
# #     answer = insert_text(text)
# #     reply = make_reply("다른식당보기", "학식")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른요일보기", "기숙사식당")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른시간보기", "화요일기숙사식당")
# #     answer = insert_replies(answer, reply)
# #
# #     return answer
#
# def get_wednesday_menu(when):
#     text = wednesday_dorm_menu(when)
#     answer = insert_text(text)
#     reply = make_reply("다른식당보기", "학식")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("다른요일보기", "기숙사식당")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("다른시간보기", "수요일기숙사식당")
#     answer = insert_replies(answer, reply)
#
#     return answer
#
# # def get_wednesday_breakfast_menu():
# #     text = wednesday_dorm_menu("breakfast")
# #     answer = insert_text(text)
# #     reply = make_reply("다른식당보기", "학식")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른요일보기", "기숙사식당")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른시간보기", "수요일기숙사식당")
# #     answer = insert_replies(answer, reply)
# #
# #     return answer
# #
# # def get_wednesday_lunch_menu():
# #     text = wednesday_dorm_menu("lunch")
# #     answer = insert_text(text)
# #     reply = make_reply("다른식당보기", "학식")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른요일보기", "기숙사식당")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른시간보기", "수요일기숙사식당")
# #     answer = insert_replies(answer, reply)
# #
# #     return answer
# #
# # def get_wednesday_dinner_menu():
# #     text = wednesday_dorm_menu("dinner")
# #     answer = insert_text(text)
# #     reply = make_reply("다른식당보기", "학식")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른요일보기", "기숙사식당")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른시간보기", "수요일기숙사식당")
# #     answer = insert_replies(answer, reply)
# #
# #     return answer
#
# def get_thursday_menu(when):
#     text = thursday_dorm_menu(when)
#     answer = insert_text(text)
#     reply = make_reply("다른식당보기", "학식")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("다른요일보기", "기숙사식당")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("다른시간보기", "목요일기숙사식당")
#     answer = insert_replies(answer, reply)
#
#     return answer
#
# # def get_thursday_breakfast_menu():
# #     text = thursday_dorm_menu("breakfast")
# #     answer = insert_text(text)
# #     reply = make_reply("다른식당보기", "학식")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른요일보기", "기숙사식당")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른시간보기", "목요일기숙사식당")
# #     answer = insert_replies(answer, reply)
# #
# #     return answer
# #
# # def get_thursday_lunch_menu():
# #     text = thursday_dorm_menu("lunch")
# #     answer = insert_text(text)
# #     reply = make_reply("다른식당보기", "학식")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른요일보기", "기숙사식당")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른시간보기", "목요일기숙사식당")
# #     answer = insert_replies(answer, reply)
# #
# #     return answer
# #
# # def get_thursday_dinner_menu():
# #     text = thursday_dorm_menu("dinner")
# #     answer = insert_text(text)
# #     reply = make_reply("다른식당보기", "학식")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른요일보기", "기숙사식당")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른시간보기", "목요일기숙사식당")
# #     answer = insert_replies(answer, reply)
# #
# #     return answer
#
# def get_friday_menu(when):
#     text = friday_dorm_menu(when)
#     answer = insert_text(text)
#     reply = make_reply("다른식당보기", "학식")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("다른요일보기", "기숙사식당")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("다른시간보기", "금요일기숙사식당")
#     answer = insert_replies(answer, reply)
#
#     return answer
# # def get_friday_breakfast_menu():
# #     text = friday_dorm_menu("breakfast")
# #     answer = insert_text(text)
# #     reply = make_reply("다른식당보기", "학식")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른요일보기", "기숙사식당")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른시간보기", "금요일기숙사식당")
# #     answer = insert_replies(answer, reply)
# #
# #     return answer
# #
# # def get_friday_lunch_menu():
# #     text = friday_dorm_menu("lunch")
# #     answer = insert_text(text)
# #     reply = make_reply("다른식당보기", "학식")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른요일보기", "기숙사식당")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른시간보기", "금요일기숙사식당")
# #     answer = insert_replies(answer, reply)
# #
# #     return answer
# #
# # def get_friday_dinner_menu():
# #     text = friday_dorm_menu("dinner")
# #     answer = insert_text(text)
# #     reply = make_reply("다른식당보기", "학식")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른요일보기", "기숙사식당")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른시간보기", "금요일기숙사식당")
# #     answer = insert_replies(answer, reply)
# #
# #     return answer
#
#
# def get_saturday_menu(when):
#     text = saturday_dorm_menu(when)
#     answer = insert_text(text)
#     reply = make_reply("다른식당보기", "학식")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("다른요일보기", "기숙사식당")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("다른시간보기", "토요일기숙사식당")
#     answer = insert_replies(answer, reply)
#
#     return answer
#
# # def get_saturday_breakfast_menu():
# #     text = saturday_dorm_menu("breakfast")
# #     answer = insert_text(text)
# #     reply = make_reply("다른식당보기", "학식")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른요일보기", "기숙사식당")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른시간보기", "토요일기숙사식당")
# #     answer = insert_replies(answer, reply)
# #
# #     return answer
# #
# # def get_saturday_lunch_menu():
# #     text = saturday_dorm_menu("lunch")
# #     answer = insert_text(text)
# #     reply = make_reply("다른식당보기", "학식")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른요일보기", "기숙사식당")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른시간보기", "토요일기숙사식당")
# #     answer = insert_replies(answer, reply)
# #
# #     return answer
# #
# # def get_saturday_dinner_menu():
# #     text = saturday_dorm_menu("dinner")
# #     answer = insert_text(text)
# #     reply = make_reply("다른식당보기", "학식")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른요일보기", "기숙사식당")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른시간보기", "토요일기숙사식당")
# #     answer = insert_replies(answer, reply)
# #
# #     return answer
# #
# # def get_sunday_breakfast_menu():
# #     text = sunday_dorm_menu("breakfast")
# #     answer = insert_text(text)
# #     reply = make_reply("다른식당보기", "학식")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른요일보기", "기숙사식당")
# #     answer = insert_replies(answer, reply)
# #     reply = make_reply("다른시간보기", "일요일기숙사식당")
# #     answer = insert_replies(answer, reply)
# #
# #     return answer
#
# def get_sunday_menu(when):
#     text = sunday_dorm_menu(when)
#     answer = insert_text(text)
#     reply = make_reply("다른식당보기", "학식")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("다른요일보기", "기숙사식당")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("다른시간보기", "일요일기숙사식당")
#     answer = insert_replies(answer, reply)
#
#     return answer

# def get_sunday_lunch_menu():
#     text = sunday_dorm_menu("lunch")
#     answer = insert_text(text)
#     reply = make_reply("다른식당보기", "학식")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("다른요일보기", "기숙사식당")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("다른시간보기", "일요일기숙사식당")
#     answer = insert_replies(answer, reply)
#
#     return answer
#
# def get_sunday_dinner_menu():
#     text = sunday_dorm_menu("dinner")
#     answer = insert_text(text)
#     reply = make_reply("다른식당보기", "학식")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("다른요일보기", "기숙사식당")
#     answer = insert_replies(answer, reply)
#     reply = make_reply("다른시간보기", "일요일기숙사식당")
#     answer = insert_replies(answer, reply)
#
#     return answer
#
