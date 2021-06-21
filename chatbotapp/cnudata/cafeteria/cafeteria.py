from chatbotapp.cnudata.cafeteria.studenthall1_info import *
# from chatbotapp.cnudata.studenthall2_info import make_answer_food_menu
from chatbotapp.cnudata.cafeteria.food_court_time import *
from chatbotapp.cnudata.cafeteria.dorm_info import *
from chatbotapp.cnudata.cafeteria.new_studenthall2_info import *


def get_entire_cafeteria_answer():
    response_text = "\n충남대학교 학식 정보\n"
    answer = insert_text(response_text)
    reply = make_reply("기숙사식당", "기숙사식당")
    answer = insert_replies(answer, reply)
    reply = make_reply("제1학생회관", "제1학생회관")
    answer = insert_replies(answer, reply)
    reply = make_reply("제2학생회관", "제2학생회관")
    answer = insert_replies(answer, reply)
    reply = make_reply("제3학생회관", "제3학생회관")
    answer = insert_replies(answer, reply)
    # reply = make_reply("🌼 제4학생회관", "제4학생회관")
    # answer = insert_replies(answer, reply)
    # reply = make_reply("🌼 생활과학대학", "생활과학대학")
    # answer = insert_replies(answer, reply)
    return answer


def get_studenthall1_answer():
    answer = category()
    return answer


def get_ramen_answer():
    answer = ramen()
    return answer


def get_gansik_answer():
    answer = gansik()
    return answer


def get_america_answer():
    answer = america()
    return answer


def get_snack_answer():
    answer = snack()
    return answer


def get_korea_answer():
    answer = korea()
    return answer


def get_japan_answer():
    answer = japan()
    return answer


def get_china_answer():
    answer = china()
    return answer


# def get_studenthall2345_answer(name):
#     response_text = f"\n😋 충남대학교 {name} 메뉴 😋    \n"
#     response_text += make_answer_food_menu(name)
#     answer = insert_text(response_text)
#     reply = make_reply("다른 식당 메뉴보기", "학식")
#     answer = insert_replies(answer, reply)
#
#     return answer

def get_studenthall23_answer(name):
    answer = get_studenthall23_answer_info(name)
    return answer


def get_entire_time():
    answer = entire_time()
    return answer


def get_ramen_time():
    answer = ramen_time()
    return answer


def get_gansik_time():
    answer = gansik_time()
    return answer


def get_america_time():
    answer = america_time()
    return answer


def get_snack_time():
    answer = snack_time()
    return answer


def get_korea_time():
    answer = korea_time()
    return answer


def get_japan_time():
    answer = japan_time()
    return answer


def get_china_time():
    answer = china_time()
    return answer


def get_entire_dorm():
    answer = dorm_time()
    return answer

# def monday_dorm():
#     answer = monday()
#     return answer
#
# def tuesday_dorm():
#     answer = tuesday()
#     return answer
#
# def wednesday_dorm():
#     answer = wednesday()
#     return answer
#
# def thursday_dorm():
#     answer = thursday()
#     return answer
#
# def friday_dorm():
#     answer = friday()
#     return answer
#
# def saturday_dorm():
#     answer = saturday()
#     return answer
#
# def sunday_dorm():
#     answer = sunday()
#     return answer
#
# def today_dorm():
#     pass


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
    text = dorm_menu("breakfast",the_day_of_week_number)
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
