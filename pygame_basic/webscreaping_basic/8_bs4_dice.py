import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=557676"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[0].a.get_text() # 지금 find_all을 통해 나온 자료값들이 cartoons에는 list형식으로 들어가져 있음.
#                                 # 그럼으로 위부터 순차적으로 0번째로 찾는것이며, a href 의 a 이후부터 글자부분만(즉 제목) 만 가져오는 문구.

# link = cartoons[0].a["href"] # 이 줄만 하면 webtoon부터 해서 링크가 가져올수 없다.
# print(title)
# print("https://comic.naver.com"+link) # 나온 결과값을 컨트롤 + 클릭시 웹페이지가 열린다.

for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com"+cartoon.a["href"]
    print(title,link)

