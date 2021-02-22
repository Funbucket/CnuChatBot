from bs4 import BeautifulSoup
import requests, re
from chatbotapp.kakaojsonformat.response import insert_text


def get_crawled_data():
    url = "https://clicker.cnu.ac.kr/Clicker/k/"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    tds = soup.find("tbody").find_all("td", attrs={"class" : re.compile("^clicker")})
    data = [i.get_text().strip() for i in tds]
    return data


def library_json_format():
    data = get_crawled_data()
    # value 값
    value = []
    for i in range(11):
        value.append("총 좌석:" + data[4 * i + 1] + " 잔여좌석:" + data[4 * i + 2] + " [" + data[4 * i + 3] + "]")

    # dict 생성
    library_info = {}
    for i in range(11):
        library_info[data[4 * i]] = value[i]
    return library_info


def get_library_answer():
    library_info = library_json_format()
    response_text = ""
    for key in library_info:
        response_text += key + "\n\t" + library_info[key] + "\n"

    answer = insert_text(response_text)
    return answer