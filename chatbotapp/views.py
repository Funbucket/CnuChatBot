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
        print("열람실")

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
    # print("return_str: {} ".format(return_str))
    # print("type : {}".format(type(return_str)))

    if return_str == "셔틀" or return_str == "✅셔틀":
        response = get_root_answer()
        return JsonResponse(response)
    # elif return_str == "A노선표보기":
    #     response = get_aroot_image("A노선표")
    #     return JsonResponse(response)
    elif return_str == "A노선":
        response = get_aroot_stations_answer()
        return JsonResponse(response)
    elif return_str == "정심화국제문화회관":
        response = get_jungsimhwa_answer()
        return JsonResponse(response)
    elif return_str == "B노선":
        response = get_broot_stations_answer()
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
