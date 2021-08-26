import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# print(soup.title) # soup을 통해 가져온 res.text에 있는 각 요소들을 접근 할수 있다.
# # print(soup.title.get_text())
# print(soup.a) # soup에 있는 데이터중에서 제일 먼저 발견되는 a의 객체 부분만 가져오기.
# print(soup.a.attrs) # a 객체가 가지고 있는 속성들을 알수 있다. 
# print(soup.a["href"]) # a 객체가 가지고 있는 속성중 특정 속성을 알고 싶을떄.

#print(soup.find("a", attrs={"class":"Nbtn_upload"})) # soup.find() : ()안에 있는 정보를 토대로 찾는다.
# print(soup.find( attrs={"class":"Nbtn_upload"})) # 네이버 올리기 버튼은 한개라서 가능하다고 한다. 정확히는 어떠한 객체든 Nbtn_upload에 해당하는 것만 찾아달라는 뜻.

        ## 우측 상단의 실행버튼 누를 시 오류가 뜨고, 메뉴에 있는 실행을 통해 하면 정상작동되는 오류 해결법
        ## pylint 설치하기.

# print(soup.find("li",attrs={"class":"rank01"}))
# rank1 = soup.find("li",attrs={"class":"rank01"}) # 자식 부분 객체를 가져오는거.
# print(rank1.a) ## 이렇게 하면 a의 객체부분만 가져올 수 있다.

# print(rank1.a.get_text())
# print(rank1.next_sibling) # 여기까지만 해서 안나오는경우는 네이버 웹툰에서 이부분이 줄바꿈으로 있어서 안나오는경우 일 수도 있다.
# print(rank1.next_sibling.next_sibling) # 그래서 다시 next_sibiling하면 뜬다.
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())

# print(rank1.parent) ## 부모 객체부분을 가져오는 것.
# rank2= rank1.find_next_sibling("li") # li에 해당하는 부분만 찾는것. 위와 다른점은 위에껀 마치 줄바꿈도 포함해서 진행하지만 이건 li부분만 해당하는 요소만 가져오는 문구.
# print(rank2.a.get_text())
# rank3 = rank2.find_previous_sibling("li")
# print(rank3.a.get_text())

# rank2 = rank1.find_next_siblings("li") # rank1을 기준으로 다음 형제들을 다 가져오는 문구.
# print(rank2)

webtoon = soup.find("a",text = "연애혁명-365. Nineteen") # text에 해당하는 글을 찾을 수 있다. 다만 연애혁명만 치면 '연애혁명'만 나올것이다.
print(webtoon)

