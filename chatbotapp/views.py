import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chatbotapp.cnudata.library import get_library_answer


@csrf_exempt
def get_library_info(request):
    answer = (request.body.decode('utf-8'))
    return_json_str = json.load(answer)
    return_str = return_json_str['userRequest']['utterance']

    if return_str == '열람실':
        response = get_library_answer()
        return JsonResponse(response)