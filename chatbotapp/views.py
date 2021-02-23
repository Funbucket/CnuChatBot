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
    elif return_str == "B2" \
        or return_str == "B1" \
        or return_str == "0" \
        or return_str == "1"\
        or return_str == "2"\
        or return_str == "3"\
        or return_str == "4"\
        or return_str == "5":

        response = each_get_library_image(return_str)
        return JsonResponse(response)




@csrf_exempt
def get_bus_info(request):
    answer = request.body.decode('utf-8')
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']

    if return_str == '셔틀':
        response = get_bus_answer()
        return JsonResponse(response)

@csrf_exempt
def get_cafeteria_info(request):
    pass

