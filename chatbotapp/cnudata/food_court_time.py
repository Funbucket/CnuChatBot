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


key = "FsSEbKLvuyBOw8JjAFaUVdG61eh6gVwOgNq7K5HNcEomRYOr2p4w%2BmI0TE4wEbYs0uR50fr4wMmhTE0sNsFq4g%3D%3D"
url = 'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService'
