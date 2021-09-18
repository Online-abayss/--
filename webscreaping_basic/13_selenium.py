# 맨처음 각 사용자의 브라우저에 맞춰서 그에 따른 드라이버를 다운받아야한다, 
# 현재 작성자는 크롬 93버전을 이용하기에 chromedriver 검색하여 맨위에 있는 사이트에 들어가서 버전에 맞는걸 들어가서 win64 이용자이지만, win32뿐이라 다운받아서 압축을 푼 ex파일을 작업하는 폴더에 넣음
import time
from selenium import webdriver

browser = webdriver.Chrome() # 현재 작성자의 폴더안에 다운받은 크롬드라이버.ex파일이 있기에 ()안에 경로를 지정하지 않았다

# 1. 네이버 이동
browser.get("http://naver.com") # browser.get을 통해 ()안의 사이트에 자동으로 크롬으로 켜준다.


# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id / pw 입력
browser.find_element_by_id("id").send_keys("secreet")
browser.find_element_by_id("pw").send_keys("unknown")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(2)



# 5. id / pw 재입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("test")
browser.find_element_by_id("id").send_keys("test")


# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
#browser.close() # 현재 탭만 종료
browser.quit() # 모든 크롬 창 종료
