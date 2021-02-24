import datetime
import requests
import xmltodict
import json

# 날짜를 요일로 변환
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week_dict = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
        weekday = datetime.datetime(year, month, day).weekday()
        return week_dict[weekday]

import requests

def get_request_query(url, operation, params, serviceKey):
    import urllib.parse as urlparse
    params = urlparse.urlencode(params)
    request_query = url + '/' + operation + '?' + params + '&' + 'serviceKey' + '=' + serviceKey
    return request_query


# 요청 URL과 오퍼레이션
URL = 'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService'
OPERATION = 'getHoliDeInfo' # 국경일 + 공휴일 정보 조회 오퍼레이션

# 파라미터
SERVICEKEY = 'FsSEbKLvuyBOw8JjAFaUVdG61eh6gVwOgNq7K5HNcEomRYOr2p4w%2BmI0TE4wEbYs0uR50fr4wMmhTE0sNsFq4g%3D%3D'
solYear  = '2018'  # 연도
solMonth = '09'   # 월
PARAMS = {'solYear':solYear, 'solMonth':solMonth}


request_query = get_request_query(URL, OPERATION, PARAMS, SERVICEKEY)
print('request_query:', request_query)
response = requests.get(url=request_query)
print(response)
print('status_code:' + str(response.status_code))
