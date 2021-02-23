import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chatbotapp.cnudata.library import *
from chatbotapp.cnudata.bus import *



@csrf_exempt
def get_library_info(request):
    answer = request.body.decode('utf-8')
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']

    if return_str == '열람실':
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

    if return_str == "셔틀":
        response = get_root_answer()
        return JsonResponse(response)

    elif return_str == "A노선":
        response = get_aroot_stations_answer()
        return JsonResponse(response)

    elif return_str == "B노선":
        response = get_broot_stations_answer()
        return  JsonResponse(response)


@csrf_exempt
def get_cafeteria_info(request):
    pass

