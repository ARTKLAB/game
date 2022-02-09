from bs4 import BeautifulSoup
import urllib.request as req

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109"

#url 열기
target = req.urlopen(url)

#데이터 분석하기
soup = BeautifulSoup(target, "html.parser")

for location in soup.select("location"):
    print("도시 : ", location.select_one("city").string)
    print("날씨 : ", location.select_one("wf").string)
    print("최저기온 : ", location.select_one("tmn").string)
    print("최고기온 : ", location.select_one("tmx").string)
    print()