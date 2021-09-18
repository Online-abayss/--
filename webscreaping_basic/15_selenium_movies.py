import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
    }

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div",attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))

# 영상에는 len이 0인 이유가 Headers 즉 이용자 주소가 해외에 잡히면 해외에서 접속이 된다.
# 또한 10개만 뜬 이유는 동적 페이지로 인해 최소 10개만 보여주고 그뒤엔 스크롤를 통해 얻어내야 한다.

for movie in movies:
    title = movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()

    print(title)
