from selenium import webdriver
# 브라우저의 로딩이 끝날 시 바로 코딩이 진행 하게 해주는 패키지라고 해야하나?
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

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

browser.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/div[1]/div/div[1]/div/fieldset/label").click()

browser.find_elements_by_link_text("제주")[0].click()

browser.find_elements_by_link_text("호텔 검색")[0].click()

## 로딩으로 인한 출력 불가로 인해 방법들 (1. 코딩 진행 속도를 지연시키기. 2. 로딩이 끝나면 바로 코딩 시작시키기.)
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='hotel:Landing_Jeju_Shinhwa_World_HotelsResorts']/div[1]" ))) ## 10초 동안 기달려주돼 어떠한 elements가 나올 때 까지.
     # By.xpath 말고도 ID, class_name, link_text 등 그 find_element_by 에서 나오는 종류들은 다 되나봄.
        # 성공시 그냥 진행 , 실패시 바로 finally로 가서 끝난다. try안에 문구가 실패시 오류가 뜬다.
    print(elem.text)
finally:
    browser.quit()


# elem = browser.find_element_by_xpath("//*[@id='hotel:Landing_Jeju_Shinhwa_World_HotelsResorts']/div[1]")

# print(elem.text)