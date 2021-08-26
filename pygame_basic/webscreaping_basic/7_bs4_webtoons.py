import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

#네이버 웹툰 전체 목록 가져오기.
cartoons = soup.find_all("a",attrs = {"class":"title"}) # 모든 정보를 가져오기 위한 find_all
for cartoon in cartoons:
    print(cartoon.get_text())

    