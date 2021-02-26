import requests
from bs4 import BeautifulSoup




soup = BeautifulSoup(r.text, "html.parser")

# select_one() 선택자
b = soup.select_one("p.title > b")
print(b)
print(b.string)
print(b.get_string)

print()

link1 = soup.select_one("#link1")
print(link1)
print(link1.text)

print()

link2 = soup.select("p.story > a")

print()

link3 = soup.select("p.story > a:nth-of-type(2)")
print(link3)

print()

link4 = soup.select("p.story")
print(link4)

print()

for i in link4:
    temp = i.find_all("a")

    if temp:
        for v in temp:
            print("----", v)
            print("----", v.string)
    else:
        print("----", i)
        print("----", i.string)
