
import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.gmarket.co.kr/?&jaehuid=200011048&gclid=Cj0KCQiAst2BBhDJARIsAGo2ldVh8nAwWtwngdkLVI%2DLOACITw4B%5F5jiTc%5FyLFzSY3AqbH4otYC%5FkTQaAvmLEALw%5FwcB")

soup = BeautifulSoup(r.text, "html.parser")
# gmaket.co.kr 1차 카테고리 명 추출 = find_all()

first_category = soup.find("span", class_="link__1depth-item")
#print(first_category)
print(first_category.string)

print()

categorys = soup.find_all("span", class_="link__1depth-item")
for categorys in first_category:
    print(categorys.string)
    

print("\n ---- 2차 카테고리")

two_categorys = soup.find_all("a", class_="link__2depth-item")
for categorys in two_categorys:
    print(categorys.string)

print()

