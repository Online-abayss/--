import requests
from bs4 import BeautifulSoup

res = requests.get("https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=2020%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84")
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

images = soup.find_all("img", attrs={"class":"thumb_img"})

for idx, image in enumerate(images):
    image_url = image["src"]
    if image_url.startswith("//"):
        image_url = "http:" + image_url

    print(image_url)
    image_res = requests.get(image_url)
    image_res.raise_for_status()

    with open("movie{}.jpg".format(idx+1),"wb") as f: # 이미지를 쓰는것이기에 w가 아닌 wb다.
        f.write(image_res.content) # 보통 문자만 있으면 res.text 일텐데 현재는 사진을 가져오는거라 content로 한것.
    
    if idx >= 4:
        break