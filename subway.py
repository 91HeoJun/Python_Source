
import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError

try:
    url = "https://ko.wikipedia.org/wiki/%EC%84%9C%EC%9A%B8_%EC%A7%80%ED%95%98%EC%B2%A0"

    with requests.Session() as s:
        # get(), soup 객체 새성
        s = requests.get("https://ko.wikipedia.org/wiki/%EC%84%9C%EC%9A%B8_%EC%A7%80%ED%95%98%EC%B2%A0")
        soup = BeautifulSoup(s.text, "html.parser")

except HTTPError as e:
    print(e)

else:
    #첫번째 이미지 가져오기
    image1 = soup.select_one("img")
    print(image1)
    print()
    #두번째 이미지 가져오기
    image2 = soup.select_one("img.thumbimage")
    print(image2)
    print()
    #첫번째 이미지 src 가져오기
    print(image1["src"])
    print()
    #두번째 이미지 src 가져오기
    print(image2["src"])