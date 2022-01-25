from bs4 import BeautifulSoup
import urllib.request as req
file=open("news.txt","w")
url="https://news.daum.net/"
result=req.urlopen(url)
soup=BeautifulSoup(result, "html.parser")

news=soup.select("div.thumb_relate")



for list in news:
    a=list.select_one("a")
    print("링크 : " +a.get('href'))
    file.write("링크 : " +a.get('href')+"\n")

    title = a.string
    print("제목 : "+title)
    file.write("제목 : "+title+"\n")

    span = list.select_one("span")
    print("언론사 : " + span.string)
    file.write("언론사 : " + span.string+"\n")

file.close()




