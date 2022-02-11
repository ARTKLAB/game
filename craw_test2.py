from bs4 import BeautifulSoup
import urllib.request as req

url = "https://news.daum.net/"

#url 열기
target = req.urlopen(url)

#데이터 분석하기
soup = BeautifulSoup(target, "html.parser")
#
# for li in soup.find("ul", "list_newsissue"):
#     a = li.find("strong")
#     if a == -1:
#         continue
#     b = a.select_one("a")
#     print("링크 : ", b.attrs["href"])
#     print("제목 : ", b.string.lstrip())
#     print()
# select("태그.클래스이름")
file = open("news.txt", "w")
news = soup.select("strong.tit_g")
for list in news:
    a = list.select_one("a")
    print("링크 : " + a.get('href'))
    file.write("링크 : " + a.get('href')+"\n")

    title = a.string
    print("제목 : " + title.strip() )
    file.write("제목 : " + title.strip() + "\n")
    print()

file.close()