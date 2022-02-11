import urllib.request

# 다운로드 할 이미지 경로
url="https://www.google.com/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.png"

# 저장할 파일 경로 및 이름
imgName = "C:\\Users\yourm\Desktop\google.png"

# 파일 다운로드
#urlretrieve(URL, 저장할 파일 경로)
urllib.request.urlretrieve(url, imgName)

print("저장완료")

from bs4 import BeautifulSoup

html = """
    <html>
    <head>
        <title>파이썬 웹 크롤링</title>
    </head>
    <body>
        <h1 id="title">안녕하세요</h1>
        <p id="name">정민수입니다.</p>
    </body>
    </html>
"""
# html 태그분석
soup = BeautifulSoup(html, 'html.parser')

'''
h1 = soup.html.body.h1
p = soup.html.body.p
'''
'''
title = soup.find("h1")
name = soup.find("p")
'''

title = soup.find(id="title")
name = soup.find(id="name")
print("title : " + title.string)
print("name : " + name.string)










