#https://finance.naver.com/main/main.nhn 

import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from fake_useragent import UserAgent

try:
    UserAgent = UserAgent()
    headers = {"user-agent": userAgent.chrome}
    url = "https://finance.naver.com"

    with requests.Session() as s:
        # get(), soup 객체 새성
        s = requests.get(url, headers=headers)
        soup = BeautifulSoup(s.text, "html.parser")

except HTTPError as e:
    print(e)

else:
    # 인기검색종목란의 이름과 가격 출력
    #container > div.aside > div.group_aside > div.aside_area.aside_popular > table > tbody > tr.down
    stocks = soup.select("div.group_aside div.aside_area.aside_popular table tbody tr")
    #print(stocks)

    for stock in stocks:
        stock_name = stock.select_one("th > a")
        stock_price = stock.find("td")
        print(stock_name.string, stock_price.string)
        