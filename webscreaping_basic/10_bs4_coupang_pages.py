import requests
from bs4 import BeautifulSoup
import re



# headers 이용할떄 {:} 세미콜론 사이 띄어쓰기 하지말기. 하면 실행 안됨.ㅋ;;
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"}
# page 1~5까지 크롤링
for i in range(1,6):
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=3&backgroundColor=".format(i)


    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    


    # 쿠팡의 노트북 이름 , 가격, 평점, 평점 수 
    for item in items:

        # 광고 제품은 제외
        ad_badge = item.find("span",attrs={"class":"ad-badge-text"})
        if ad_badge:
            print("--- 광고 상품 제외합니다. ---")
            continue

        name = item.find("div", attrs={"class":"name"}).get_text()

        # 에이수스 제품 제외
        if "에이수스" in name:
            # print(" --- 에이수스 상품은 제외합니다. ---")
            continue

        price = item.find("strong", attrs={"class":"price-value"}).get_text()

        #5 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회 
        rate = item.find("em", attrs={"class":"rating"})
        if rate:
            rate = rate.get_text()
        else:
            # print(" --- 평점 없는 상품은 제외합니다. ---")
            continue
            
        rate_cut = item.find("span", attrs={"class":"rating-total-count"})
        if rate_cut:
            rate_cut = rate_cut.get_text()[1:-1]
             # 1 index부터 뒤에서 1 index까지 가져오기.
        else:
            # print(" --- 평점 수 없는 상품은 제외합니다. ---")
            continue
        link = item.find("a",attrs={"class":"search-product-link"})["href"]

        if float(rate) >= 4.5 and int(rate_cut) >= 100:
            # print(name,price,rate,rate_cut)
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate} ({rate_cut}개)")
            print("바로가기 :{}".format("https://www.coupang.com"+link))
            print("-"*50)
            