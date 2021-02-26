#https://news.v.daum.net/v/20210226111838232

import requests
from bs4 import BeautifulSoup

r = requests.get("https://news.v.daum.net/v/20210226111838232")

soup = BeautifulSoup(r.text, "html.parser")

# 1. 뉴스 제목 출력하기
# 1-1. find 방법 사용
news_title = soup.select_one(".tit_view")
print(news_title)
print(news_title.string)
print()

# 1-2title 태그 방법 사용
print(soup.title.get_text())
print()

# 2. 기사 작성시간 출력하기
num_date = soup.select_one("span", class_="num_date")
print(num_date)
print(num_date.string)
print()

# 3. 기사 첫번쨰 문단 출력하기
#paragraph = soup.select_one("p", {"dmcf-pid": "cOeD2HXtps"})
paragraph = soup.select_one("p[dmcf-pid='cOeD2HXtps']")
print(paragraph)
print(paragraph.string)
print()

#paragraph = soup.select_one("p[dmcf-pid:'cOeD2HXtps']")
#print(paragraph)
#print(paragraph.string) 

# 기사 작성자 출력하기
writer = soup.select_one("span", class_="txt_info")
print(writer)
print(writer.string)


