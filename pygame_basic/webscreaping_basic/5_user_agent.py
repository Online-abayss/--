import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}

res = requests.get(url, headers=headers) # 영상에서는 티스토리가 접속하는걸 정상적인 방법으로 접속하지 않는다고 판단해서 정상코드를 보내주지 않음 
# 그래서 위의 headers를 통해 값을 구해서 직접 사람이 들어가는 정상루트라는걸 입증해서 들어가서 html 파일들을 구하게 됨
# headers를 구하는법은 구글에 User Agent String 이라고 치면 whatismyuseragent 하는 홈페이지 들가면 값을 볼수 있다.
print("응답코드 : ", res.status_code)
res.raise_for_status()
with open("nadocoding.html", "w",encoding="utf8") as f:
    f.write(res.text)
