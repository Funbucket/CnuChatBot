import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chatbotapp.cnudata.library import get_library_answer


@csrf_exempt
def message(request):
    answer = (request.body.decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']

    if return_str == '테스트':
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': "테스트 성공입니다."
                    }
                }],
                'quickReplies': [{
                    'label': '처음으로',
                    'action': 'message',
                    'messageText': '처음으로'
                }]
            }
        })


@csrf_exempt
def get_library_info(request):
    answer = (request.body.decode('utf-8'))
    return_json_str = json.load(answer)
    return_str = return_json_str['userRequest']['utterance']

    if return_str == '열람실':
        response = get_library_answer()
        return JsonResponse(response)