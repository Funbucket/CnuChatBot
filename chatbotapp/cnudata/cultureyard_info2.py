from bs4 import BeautifulSoup
import requests, re

url = "https://plus.cnu.ac.kr/_prog/_board/?code=sub07_070801&site_dvs_cd=kr&menu_dvs_cd=070801"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')

titles = soup.find("tbody").find_all("td", attrs={"class": re.compile("[^title nt]")})
# info_titles = soup.find("tbody").find_all("td", attrs={"class": "title nt"})

print(len(titles))

# with open("test.html", "w", encoding="utf-8") as f:
#     f.write(soup.prettify())