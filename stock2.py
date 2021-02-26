#https://finance.naver.com/main/

import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError

try:
    url = "https://finance.naver.com"

    with requests.Session() as s:
        # get(), soup 객체 새성
        s = requests.get(url)
        soup = BeautifulSoup(s.text, "html.parser")

except HTTPError as e:
    print(e)

else:
    # 해외증시 종목란의 이름과 가격 출력
    # container > div.aside > div.group_aside > div.aside_area.aside_stock > table > tbody > tr:nth-child(1)
    stocks = soup.select(
        "div.group_aside  div.aside_area.aside_stock  table  tbody  tr"
        )
    #print(stocks)

    for stock in stocks:
        stock_name = stock.select_one("th > a")
        stock_price = stock.find("td")
        print(stock_name.string, stock_price.string)
        