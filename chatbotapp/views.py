import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chatbotapp.cnudata.library import *
from chatbotapp.cnudata.bus import *
from chatbotapp.cnudata.cafeteria import *
from chatbotapp.cnudata.etc import *


@csrf_exempt
def get_library_info(request):
    answer = request.body.decode('utf-8')
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']
    print("return_str : {}".format(return_str))

    if return_str == "열람실" or return_str == "✅열람실":
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

    if return_str == "셔틀" or return_str == "✅셔틀":
        response = get_root_answer()
        return JsonResponse(response)
    elif return_str == "(A)다른정류장보기":
        response = get_aroot_stations_answer()
        return JsonResponse(response)
    elif return_str == "(B)다른정류장보기":
        response = get_broot_stations_answer()
        return JsonResponse(response)
    elif return_str == "다른노선보기":
        response = get_root_answer()
        return JsonResponse(response)
    elif return_str == "A노선":
        response = get_aroot_stations_answer()
        return JsonResponse(response)
    elif return_str == "A정심화국제문화회관":
        response = get_aline_arriving_time_answer(8, 30)
        return JsonResponse(response)
    elif return_str == "A경상대학앞":
        response = get_aline_arriving_time_answer(8, 31)
        return JsonResponse(response)
    elif return_str == "A도서관 앞(농대방향)":
        response = get_aline_arriving_time_answer(8, 32)
        return JsonResponse(response)
    elif return_str == "A학생생활관3거리":
        response = get_aline_arriving_time_answer(8, 33)
        return JsonResponse(response)
    elif return_str == "A농업생명과학대학 앞(동문주자창 방향)":
        response = get_aline_arriving_time_answer(8, 34)
        return JsonResponse(response)
    elif return_str == "A동문주차장":
        response = get_aline_arriving_time_answer(8, 35)
        return JsonResponse(response)
    elif return_str == "A농업생명과학대학 앞":
        response = get_aline_arriving_time_answer(8, 36)
        return JsonResponse(response)
    elif return_str == "A도서관앞(도서관 삼거리 방향)":
        response = get_aline_arriving_time_answer(8, 37)
        return JsonResponse(response)
    elif return_str == "A예술대학앞":
        response = get_aline_arriving_time_answer(8, 38)
        return JsonResponse(response)
    elif return_str == "A음악2호관앞":
        response = get_aline_arriving_time_answer(8, 39)
        return JsonResponse(response)
    elif return_str == "A공동동물실험센터 입구(회차)":
        response = get_aline_arriving_time_answer(8, 40)
        return JsonResponse(response)
    elif return_str == "A체육관 입구":
        response = get_aline_arriving_time_answer(8, 41)
        return JsonResponse(response)
    elif return_str == "A서문(공동실험실습관앞)":
        response = get_aline_arriving_time_answer(8, 42)
        return JsonResponse(response)
    elif return_str == "A사회과학대학 입구(한누리회관뒤)":
        response = get_aline_arriving_time_answer(8, 43)
        return JsonResponse(response)
    elif return_str == "A산학연교육연구관앞":
        response = get_aline_arriving_time_answer(8, 44)
        return JsonResponse(response)

    elif return_str == "B노선":
        response = get_broot_stations_answer()
        return JsonResponse(response)
    elif return_str == "B정심화국제문화회관":
        response = get_bline_arriving_time_answer(8, 30)
        return JsonResponse(response)
    elif return_str == "B사회과학대학입구(한누리회관뒤)":
        response = get_bline_arriving_time_answer(8, 31)
        return JsonResponse(response)
    elif return_str == "B서문(공동실험실습관앞)":
        response = get_bline_arriving_time_answer(8, 32)
        return JsonResponse(response)
    elif return_str == "B음악2호관앞":
        response = get_bline_arriving_time_answer(8, 33)
        return JsonResponse(response)
    elif return_str == "B공동동물실험센터입구(회차)":
        response = get_bline_arriving_time_answer(8, 34)
        return JsonResponse(response)
    elif return_str == "B체육관입구":
        response = get_bline_arriving_time_answer(8, 35)
        return JsonResponse(response)
    elif return_str == "B예술대학앞":
        response = get_bline_arriving_time_answer(8, 36)
        return JsonResponse(response)
    elif return_str == "B도서관앞(대학본부옆농대방향)":
        response = get_bline_arriving_time_answer(8, 37)
        return JsonResponse(response)
    elif return_str == "B농업생명과학대학 앞":
        response = get_bline_arriving_time_answer(8, 38)
        return JsonResponse(response)
    elif return_str == "B동문주차장":
        response = get_bline_arriving_time_answer(8, 39)
        return JsonResponse(response)
    elif return_str == "B농업생명과학대학앞":
        response = get_bline_arriving_time_answer(8, 40)
        return JsonResponse(response)
    elif return_str == "B학생생활관3거리":
        response = get_bline_arriving_time_answer(8, 41)
        return JsonResponse(response)
    elif return_str == "B도서관앞(도서관삼거리 방향)":
        response = get_bline_arriving_time_answer(8, 42)
        return JsonResponse(response)
    elif return_str == "B공과대학앞":
        response = get_bline_arriving_time_answer(8, 43)
        return JsonResponse(response)
    elif return_str == "B산학연교육연구관앞":
        response = get_bline_arriving_time_answer(8, 44)
        return JsonResponse(response)


@csrf_exempt
def get_cafeteria_info(request):
    answer = request.body.decode('utf-8')
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']

    if return_str == "학식" or return_str == "✅학식":
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

    elif return_str == "제2학생회관(인재개발원)" \
            or return_str == "제3학생회관" \
            or return_str == "제4학생회관" \
            or return_str == "생활과학대학":
        response = get_studenthall2345_answer(return_str)
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

    elif return_str == "월요일기숙사식당":
        response = monday_dorm()
        return JsonResponse(response)

    elif return_str == "화요일기숙사식당":
        response = tuesday_dorm()
        return JsonResponse(response)

    elif return_str == "수요일기숙사식당":
        response = wednesday_dorm()
        return JsonResponse(response)

    elif return_str == "목요일기숙사식당":
        response = thursday_dorm()
        return JsonResponse(response)

    elif return_str == "금요일기숙사식당":
        response = friday_dorm()
        return JsonResponse(response)

    elif return_str == "토요일기숙사식당":
        response = saturday_dorm()
        return JsonResponse(response)

    elif return_str == "일요일기숙사식당":
        response = sunday_dorm()
        return JsonResponse(response)

    elif return_str == "월[아침]":
        response = get_monday_breakfast_menu()
        return JsonResponse(response)
    elif return_str == "월[점심]":
        response = get_monday_lunch_menu()
        return JsonResponse(response)

    elif return_str == "월[저녁]":
        response = get_monday_dinner_menu()
        return JsonResponse(response)

    elif return_str == "화[아침]":
        response = get_tuesday_breakfast_menu()
        return JsonResponse(response)
    elif return_str == "화[점심]":
        response = get_tuesday_lunch_menu()
        return JsonResponse(response)
    elif return_str == "화[저녁]":
        response = get_tuesday_dinner_menu()
        return JsonResponse(response)

    elif return_str == "수[아침]":
        response = get_wednesday_breakfast_menu()
        return JsonResponse(response)
    elif return_str == "수[점심]":
        response = get_wednesday_lunch_menu()
        return JsonResponse(response)
    elif return_str == "수[저녁]":
        response = get_wednesday_dinner_menu()
        return JsonResponse(response)

    elif return_str == "목[아침]":
        response = get_thursday_breakfast_menu()
        return JsonResponse(response)
    elif return_str == "목[점심]":
        response = get_thursday_lunch_menu()
        return JsonResponse(response)
    elif return_str == "목[저녁]":
        response = get_thursday_dinner_menu()
        return JsonResponse(response)

    elif return_str == "금[아침]":
        response = get_friday_breakfast_menu()
        return JsonResponse(response)
    elif return_str == "금[점심]":
        response = get_friday_lunch_menu()
        return JsonResponse(response)
    elif return_str == "금[저녁]":
        response = get_friday_dinner_menu()
        return JsonResponse(response)

    elif return_str == "토[아침]":
        response = get_saturday_breakfast_menu()
        return JsonResponse(response)
    elif return_str == "토[점심]":
        response = get_saturday_lunch_menu()
        return JsonResponse(response)
    elif return_str == "토[저녁]":
        response = get_saturday_dinner_menu()
        return JsonResponse(response)

    elif return_str == "일[아침]":
        response = get_sunday_breakfast_menu()
        return JsonResponse(response)
    elif return_str == "일[점심]":
        response = get_sunday_lunch_menu()
        return JsonResponse(response)
    elif return_str == "일[저녁]":
        response = get_sunday_dinner_menu()
        return JsonResponse(response)

@csrf_exempt
def get_etc_info(request):
    answer = request.body.decode('utf-8')
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']
    if return_str == "기타" or return_str == "✅기타":
        response = get_entire_etc_answer()
        return JsonResponse(response)

    elif return_str == "📬오류 제보 / 기능 건의📬" or return_str == "오류 제보/기능 건의":
        response = get_error_answer()
        return JsonResponse(response)

    elif return_str == "ℹ️개발자 정보" or return_str == "개발자 정보":
        response = get_information_answer()
        return JsonResponse(response)
