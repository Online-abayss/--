# 정규식. [ 특정한 규칙으로 정해진 문구로 그에 부합하는지 여부를 판단. ex) : 주민등록번호 999999-5678699 x, 000111-3456123 o]

import re

p = re.compile("ca.e") # ca?e 중 cae만 알경우 ca.e로 쓴다. 
# . (ca.e): 하나의 문자로 취급 ex) : care, cafe, case ...
# ^ (^de): 문자열의 시작 > ex) : desk, destination ...
# $ (se$): 문자열의 끝 > ex) : case, base ...

def print_match(m):


    if m :
        print("m.group():", m.group()) # 일치하는 문자열 반환
        print("m.string : ", m.string) # 입력받은 문자열
        print("m.start() : ", m.start()) # 일치하는 문자열의 시작 index
        print("m.end()", m.end()) # 일치하는 문자열의 끝 index 
        print("m.span()", m.span()) # 일치하는 문자열의 시작 / 끝 index
    else: 
        print("매칭되지 않음")

#m = p.match("case")
#m = p.match("careless") # 주어진 문자열의 처음부터 일치하는지 확인 . [ 그래서 care부분이 일치한다고 출력이 뜬다.] 
#print(m.group()) # 매치가 안되면 에러가 발생 / 매치가 되었을 경우 출력.
#print_match(m)

# m = p.search("careless") # search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

# lst = p.findall("good care cafe") # findall : 일치하는 모든 것을 리시트 형태로 반환
# print(lst)

# 1. p= re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m - p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환

# . (ca.e): 하나의 문자로 취급 ex) : care, cafe, case ...
# ^ (^de): 문자열의 시작 > ex) : desk, destination ...
# $ (se$): 문자열의 끝 > ex) : case, base ...
