import requests
res = requests.get("http://google.com")
res.raise_for_status()
#print("웹 스크래핑을 시진행합니다.") # 만약 res의 주소값이 문제가 생겼을 경우 바로 오류를 일으켜 중단시킨다.

#print("응답 코드 : ",res.status_code) # 200이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다. [에러코드 ",res.status_code,"]")


print(len(res.text))
print(res.text)

with open("myopen.html", "w",encoding="utf8") as f:
    f.write(res.text)