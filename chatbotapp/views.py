import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chatbotapp.cnudata.library.library import *
from chatbotapp.cnudata.cafeteria.cafeteria import *
from chatbotapp.cnudata.etc import *
from chatbotapp.cnudata.organized_information.arcademic_info import *
from chatbotapp.cnudata.organized_information.cultureyard_info import *
from chatbotapp.cnudata.organized_information.phonenumber import *
from chatbotapp.cnudata.organized_information.study_competition import get_study_competition_answer
from chatbotapp.cnudata.organized_information.cnumarket import get_cnumarket_answer
from chatbotapp.cnudata.shuttlebus.bus import *
from chatbotapp.cnudata.is_vacation import get_vacation

import datetime


@csrf_exempt
def get_library_info(request):
    answer = request.body.decode('utf-8')
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']

    if return_str == "열람실" or return_str == "📚 열람실" :
        response = get_library_answer()
        return JsonResponse(response)

    elif return_str == "B2 Learning Commons" \
        or return_str == "B2 Carrel Zone" \
        or return_str == "1층 자유열람실" \
        or return_str == "2층 제 1열람실 A"\
        or return_str == "2층 제 1열람실 B"\
        or return_str == "2층 제 2열람실 A"\
        or return_str == "2층 제 2열람실 B"\
        or return_str == "2층 제 2열람실 노트북석"\
        or return_str == "2층 제 3열람실 A"\
        or return_str == "2층 제 3열람실 B"\
        or return_str == "2층 제 3열람실 노트북실":

        response = each_get_library_answer(return_str)

        return JsonResponse(response)

    elif return_str == "층별지도보기":
        response = entire_floor_image()
        return JsonResponse(response)

    elif return_str == "B2층 지도보기" \
        or return_str == "B1층 지도보기" \
        or return_str == "별관1층 지도보기" \
        or return_str == "1층 지도보기"\
        or return_str == "2층 지도보기"\
        or return_str == "3층 지도보기"\
        or return_str == "4층 지도보기"\
        or return_str == "5층 지도보기":

        response = each_get_library_image(return_str)
        return JsonResponse(response)


@csrf_exempt
def get_bus_info(request):
    answer = request.body.decode('utf-8')
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']
    if return_str == "셔틀" or return_str == "🚌 셔틀":
        '''response = get_root_answer()
        return JsonResponse(response)'''
        if get_vacation():
            response = get_holiday_bus_answer()
        else:
            response = get_root_answer()
        return JsonResponse(response)
    elif return_str == "A노선":
        response = get_aroot_answer()
        return JsonResponse(response)
    elif return_str == "B노선":
        response = get_broot_answer()
        return JsonResponse(response)
    elif return_str == "C노선":
        response = get_croot_answer()
        return JsonResponse(response)
    elif return_str == "오전":
        response = get_croot_am_answer()
        return JsonResponse(response)
    elif return_str == "오후":
        response = get_croot_pm_answer()
        return JsonResponse(response)
    elif return_str == "A노선표":
        response = get_aroot_image()
        return JsonResponse(response)
    elif return_str == "B노선표":
        response = get_broot_image()
        return JsonResponse(response)
    elif return_str == "C노선표":
        response = get_croot_image()
        return JsonResponse(response)


@csrf_exempt
def get_cafeteria_info(request):
    answer = request.body.decode('utf-8')
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']
    today_week_number = datetime.datetime.today().weekday() + 1
    if return_str == "학식" or return_str == "🍽 학식":
        response = get_entire_cafeteria_answer()
        return JsonResponse(response)

    elif return_str == "제1학생회관":
        response = get_studenthall1_answer()
        return JsonResponse(response)

    elif return_str == "라면&우동":
        response = get_ramen_answer()
        return JsonResponse(response)

    elif return_str == "간식":
        response = get_gansik_answer()
        return JsonResponse(response)

    elif return_str == "양식":
        response = get_america_answer()
        return JsonResponse(response)

    elif return_str == "스낵":
        response = get_snack_answer()
        return JsonResponse(response)

    elif return_str == "한식":
        response = get_korea_answer()
        return JsonResponse(response)

    elif return_str == "일식":
        response = get_japan_answer()
        return JsonResponse(response)

    elif return_str == "중식":
        response = get_china_answer()
        return JsonResponse(response)

    elif return_str == "제2학생회관" \
            or return_str == "제3학생회관":
        response = get_studenthall23_answer(return_str)
        return JsonResponse(response)

    elif return_str == "운영시간":
        response = get_entire_time()
        return JsonResponse(response)

    elif return_str == "라면코너 운영 시간":
        response = get_ramen_time()
        return JsonResponse(response)

    elif return_str == "간식코너 운영 시간":
        response = get_gansik_time()
        return JsonResponse(response)

    elif return_str == "양식코너 운영 시간":
        response = get_america_time()
        return JsonResponse(response)

    elif return_str == "스낵코너 운영 시간":
        response = get_snack_time()
        return JsonResponse(response)

    elif return_str == "한식코너 운영 시간":
        response = get_korea_time()
        return JsonResponse(response)

    elif return_str == "일식코너 운영 시간":
        response = get_japan_time()
        return JsonResponse(response)

    elif return_str == "중식코너 운영 시간":
        response = get_china_time()
        return JsonResponse(response)
    elif return_str == "기숙사식당":
        response = get_entire_dorm()
        return JsonResponse(response)

    elif return_str == "오늘기숙사식당":
        response = day_of_week_dorm(today_week_number)
        return JsonResponse(response)

    elif return_str == "월요일기숙사식당":
        response = day_of_week_dorm(1)
        return JsonResponse(response)

    elif return_str == "화요일기숙사식당":
        response = day_of_week_dorm(2)
        return JsonResponse(response)

    elif return_str == "수요일기숙사식당":
        response = day_of_week_dorm(3)
        return JsonResponse(response)

    elif return_str == "목요일기숙사식당":
        response = day_of_week_dorm(4)
        return JsonResponse(response)

    elif return_str == "금요일기숙사식당":
        response = day_of_week_dorm(5)
        return JsonResponse(response)

    elif return_str == "토요일기숙사식당":
        response = day_of_week_dorm(6)
        return JsonResponse(response)

    elif return_str == "일요일기숙사식당":
        response = day_of_week_dorm(7)
        return JsonResponse(response)

    elif return_str == "월[아침]":
        response = get_entire_menu("breakfast",Weekday.MONDAY.value)
        return JsonResponse(response)
    elif return_str == "월[점심]":
        response = get_entire_menu("lunch",Weekday.MONDAY.value)
        return JsonResponse(response)
    elif return_str == "월[저녁]":
        response = get_entire_menu("dinner",Weekday.MONDAY.value)
        return JsonResponse(response)

    elif return_str == "화[아침]":
        response = get_entire_menu("breakfast",Weekday.TUESDAY.value)
        return JsonResponse(response)
    elif return_str == "화[점심]":
        response = get_entire_menu("lunch",Weekday.TUESDAY.value)
        return JsonResponse(response)
    elif return_str == "화[저녁]":
        response = get_entire_menu("dinner",Weekday.TUESDAY.value)
        return JsonResponse(response)

    elif return_str == "수[아침]":
        response = get_entire_menu("breakfast",Weekday.WEDNESDAY.value)
        return JsonResponse(response)
    elif return_str == "수[점심]":
        response = get_entire_menu("lunch",Weekday.WEDNESDAY.value)
        return JsonResponse(response)
    elif return_str == "수[저녁]":
        response = get_entire_menu("dinner",Weekday.WEDNESDAY.value)
        return JsonResponse(response)

    elif return_str == "목[아침]":
        response = get_entire_menu("breakfast",Weekday.THURSDAY.value)
        return JsonResponse(response)
    elif return_str == "목[점심]":
        response = get_entire_menu("lunch",Weekday.THURSDAY.value)
        return JsonResponse(response)
    elif return_str == "목[저녁]":
        response = get_entire_menu("dinner",Weekday.THURSDAY.value)
        return JsonResponse(response)

    elif return_str == "금[아침]":
        response = get_entire_menu("breakfast",Weekday.FRIDAY.value)
        return JsonResponse(response)
    elif return_str == "금[점심]":
        response = get_entire_menu("lunch",Weekday.FRIDAY.value)
        return JsonResponse(response)
    elif return_str == "금[저녁]":
        response = get_entire_menu("dinner",Weekday.FRIDAY.value)
        return JsonResponse(response)

    elif return_str == "토[아침]":
        response = get_entire_menu("breakfast",Weekday.SATURDAY.value)
        return JsonResponse(response)
    elif return_str == "토[점심]":
        response = get_entire_menu("lunch",Weekday.SATURDAY.value)
        return JsonResponse(response)
    elif return_str == "토[저녁]":
        response = get_entire_menu("dinner",Weekday.SATURDAY.value)
        return JsonResponse(response)

    elif return_str == "일[아침]":
        response = get_entire_menu("breakfast",Weekday.SUNDAY.value)
        return JsonResponse(response)
    elif return_str == "일[점심]":
        response = get_entire_menu("lunch",Weekday.SUNDAY.value)
        return JsonResponse(response)
    elif return_str == "일[저녁]":
        response = get_entire_menu("dinner",Weekday.SUNDAY.value)
        return JsonResponse(response)


@csrf_exempt
def get_etc_info(request):
    answer = request.body.decode('utf-8')
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']
    if return_str == "기타" or return_str == "🎸 기타":
        response = get_entire_etc_answer()
        return JsonResponse(response)

    elif return_str == "📬오류 제보 / 기능 건의📬" or return_str == "오류 제보/기능 건의":
        response = get_error_answer()
        return JsonResponse(response)

    elif return_str == "ℹ️개발자 정보" or return_str == "개발자 정보":
        response = get_information_answer()
        return JsonResponse(response)


@csrf_exempt
def get_cnunews(request):
    answer = request.body.decode('utf-8')
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']
    if return_str == "알뜰정보" or return_str == "📰 알뜰정보":
        response = insert_text("😋 충남대학교 알뜰 정보 😋")
        reply = make_reply("학사정보", "학사정보")
        response = insert_replies(response, reply)
        reply = make_reply("문화마당", "문화마당")
        response = insert_replies(response, reply)
        reply = make_reply("CNU장터", "CNU장터")
        response = insert_replies(response, reply)
        reply = make_reply("스터디 및 공모전", "스터디 및 공모전")
        response = insert_replies(response, reply)
        reply = make_reply("각종전화번호", "각종전화번호")
        response = insert_replies(response, reply)
        return JsonResponse(response)
    elif return_str == "학사정보":
        response = get_arcademic_answer()
        return JsonResponse(response)
    elif return_str == "문화마당":
        response = get_cultureyard_answer()
        return JsonResponse(response)
    elif return_str == "각종전화번호":
        response = get_phone_number_answer()
        return JsonResponse(response)
    elif return_str == "스터디 및 공모전":
        response = get_study_competition_answer()
        return JsonResponse(response)
    elif return_str == "CNU장터":
        response = get_cnumarket_answer()
        return JsonResponse(response)
