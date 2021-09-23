from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

chromedriver = './chromedriver' 
driver = webdriver.Chrome(chromedriver, options=options )
driver.get('https://entertain.daum.net/') 
print(driver.title) 
print(driver.current_url)

options.headless = True
options.add_argument("window-size=1366*768")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

# 지정한 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0,768)") # 해상도에 따라 다름. # 정확히는 얼만큼 내릴건지 설정하는거. 굳이 해상도 까지 안해도됨.

# 화면 가장 아래로 스크롤 내리기
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

import time
interval = 10

# 현재 문서 높이 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤 내리기
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # 로딩 대기
    time.sleep(interval)
    # 현재 문서 높이 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print(" 스크롤 완료 ")

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div",attrs={"class":"Vpfmgd"}) # 만약 다른 elem을 추가하고싶으면 리스트로 추가하면된다.
print(len(movies))

# 영상에는 len이 0인 이유가 Headers 즉 이용자 주소가 해외에 잡히면 해외에서 접속이 된다.
# 또한 10개만 뜬 이유는 동적 페이지로 인해 최소 10개만 보여주고 그뒤엔 스크롤를 통해 얻어내야 한다.

for movie in movies:
    title = movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()

    # 할인 전 가격
    original_price = movie.find("span",attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, "<할인되지 않는 영화 제외").
        continue

    # 할인된 가격
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크
    link = movie.find("a",attrs={"class":"JC71ub"})["href"]
    
    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : " , "https://play.google.com" + link)
    print("-"*50)

browser.quit()
