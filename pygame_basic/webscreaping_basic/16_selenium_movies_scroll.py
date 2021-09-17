# import requests
# from bs4 import BeautifulSoup

# url = "https://play.google.com/store/movies/top"
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
#     "Accept-Language":"ko-KR,ko"
#     }

# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# movies = soup.find_all("div",attrs={"class":"ImZGtf mpg5gc"})
# print(len(movies))

# # 영상에는 len이 0인 이유가 Headers 즉 이용자 주소가 해외에 잡히면 해외에서 접속이 된다.
# # 또한 10개만 뜬 이유는 동적 페이지로 인해 최소 10개만 보여주고 그뒤엔 스크롤를 통해 얻어내야 한다.

# for movie in movies:
#     title = movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()

#     print(title)


from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

# 지정한 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0,768)") # 해상도에 따라 다름. # 정확히는 얼만큼 내릴건지 설정하는거. 굳이 해상도 까지 안해도됨.

# 화면 가장 아래로 스크롤 내리기
browser.execute_script("window.scrollTo(0,document.body.scrollHieght)")

import time
interval = 2 

# 현재 문서 높이 저장
prev_height = browser.execute_script("return document.body.scrollHieght")

# 반복 수행
while True:
    # 스크롤 내리기
    browser.execute_script("window.scrollTo(0,document.body.scrollHieght)")
    # 로딩 대기
    time.sleep(interval)
    # 현재 문서 높이 저장
    curr_height = browser.execute_script("return document.body.scrollHieght")
    if curr_height == prev_height:
        break

    