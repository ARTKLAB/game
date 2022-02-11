from bs4 import BeautifulSoup

html = """
    <html>
    <head>
        <title>find_all()</title>
    </head>
    <body>
        <ul>
            <li>
                <a href="http://www.naver.com">네이버</>
            </li>
            <li>
                <a href="http://www.google.com">구글</a>
            </li>
        </ul>
    </body>
    </html>
"""
# html 태그분석
soup = BeautifulSoup(html, 'html.parser')
list = soup.findAll("a")

# print(list[0])
# print(list[1])
#태그안에
for a in list:
    #text = a.string
    #print(text)
    href = a.attrs["href"]
    print(href)









