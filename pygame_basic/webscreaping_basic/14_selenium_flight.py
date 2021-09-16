from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/"
browser.get(url)

# browser.find_element_by_link_text("웹툰").click()


# 21.09.16일 기준으로 영상과 다르게 페이지의 변화도 있고. 명칭과 그대로 적용이 안됨... 그러므로 호텔로 대신함
# browser.find_element_by_link_text("가는 날").click() 

browser.find_element_by_link_text("호텔").click()

browser.find_element_by_link_text("체크인").click()

browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번달 / 27이라는 문자는 다음달에도 있는 2개 이상의 중복문자이기에 elements를 쓴다.

browser.find_elements_by_link_text("29")[0].click()
