
# if 조건식 : 
# #    실행문
# num = 10
# if num > 5:
#     print("크다")
#     print("10이크다")
# elif num < 5:
#     print("작다")
#     print("5보다 작다")
# else:
#     print("같다")
#     print("5와 같다")


# 변수 apple의 값이 10이상이라면 1봉지 8000원 이라고 출력
# 변수 apple의 값이 10미만이라면 개당 2000원 출력 
# apple = 10
# if(apple>=10):
#     print("1봉지 8000원")
# else:
#     print("개당 2000원")

# res = 2
# match res:
#     case 1|4:
#         print("1입니다")
#     case 2:
#         print("2입니다")
#     case int():
#         print("정수 이다")

# like = 100
# match like:
#     case a if a >= 100:
#         print("spot 등록")
#     case a if a <= 10:
#         print("관심 스팟")


# 아이디 와 비밀번호 입력 받아 일치하면 로그인 성공 , 일치하지 않으면 아이디 또는 비밀번호가 잘못 되었습니다 출력
# 아이디는 진섭 , 비밀번호는 babo 

# id = input("아이디 입력 : ")
# pw = input("비밀번호 입력 : ")

# if id == "진섭" and pw == "babo":
#     print("로그인 성공")
# else:
#     print("아이디 또는 비밀번호가 잘못 되었습니다")
    
# word = " 나는 김진섭 입니다."
# if '김진섭' in word:
#     print("있다")
# else:
#     print("없다")

# word = " 나는 진섭이가 짝꿍일때 별로 였다."

# # word 안에 동렬 이름이 없다라는 것을  확인 할 수 있는 코드

# if '동렬' not in word:
#     print("동렬이 없다")
# else:    
#     print("동렬이 있다")

# # startswith : 문자열이 특정 문자로 시작하는지 확인
# # endswith : 문자열이 특정 문자로 끝나는지 확인
# word = "차도헌 님 께서 입장 하셨습니다."
# if word.startswith("이창호"):
#     print("신원 확인")
# else:
#     print("신원 불명")

# word = "i like banana"
# print(word.upper())  #대문자
# print(word.lower())  #소문자
# print(word.title())  #각 단어의 첫 글자 대문자

# #공백제거 - 개발시 필요필수 (이거 때문에 오류나면 골치아픔)
# word = "   hello world    "
# print(word.strip())  # 양쪽 공백 제거
# print(word.lstrip()) # 왼쪽 공백 제거
# print(word.rstrip()) # 오른쪽 공백 제거

# # 찾기 
# word= "찬용이는 진섭이보다 지금이 좋다고 한다."
# print( word.find("창호")) # 있다면 위치 반환(인덱스) 없으면 -1
# # print(word.index("동렬")) # 있다면 위치 반환(인덱스) 없으면 오류 발생

# # 문자열 바꾸기   .replace("현재 문자열에서 변경 할 문자열","바꿀 문자열")
# word = word.replace("찬용이","성현이")
# print(word)

# # 문자열 나누기 - 배열
# text = "도헌-지연-동렬-진섭"
# fruits = text.split("-")
# print(fruits)

# #  배열을 문자열로 합치기
# # fruits = ["도헌","지연","동렬","진섭"]
# result = ",".join(fruits)
# print(result)

# # 숫자인지 아닌지 판별
# text = "12345"
# print(text.isdigit()) # 문자열을 숫자로 변환하기 전에 확인하느 용도 

# # 문자 종류 확인
# text1 = "tomato"
# text2 = "  "
# text3 = "사월22"
# print( text2.isalpha() ) # 문자로만 이루어 져 있는지 확인 (공백있으면 False)
# print( text2.isspace() ) # 공백으로만 이루어 져 있는지 확인 
# print( text3.isalnum() ) # 문자와 숫자로만 이루어 져 있는지 확인 (공백있으면 False)

# # 문자열 정렬
# text = "15"
# print( text.zfill(6)) # 문자열의 길이가 6이 될 때까지 0으로 채워라 (오른쪽 정렬)
# print( text.rjust(4))
# print( text.ljust(4,"*"))

# u = input("아이디 입력 : ")

# print( u.strip().lower())

# 문제2. - "행복,우울,기쁨,슬픔,화남"
# 위 문자열을 나누어 보세요
# text = "행복,우울,기쁨,슬픔,화남"
# print(text.split(","))

# 문제3. 회원가입시 이메일 입력을 하는데 특정 주소만 가능하다.
# naver.com, gmail.com , nate.com , daum.net 
# # 위 4개만 가능하다 input으로 이메일을 입력 받아서 가입인지 불가능인지 판별
# email = input("이메일 : ").strip().lower() 
# if email.endswith("naver.com") or email.endswith("gmail.com") or email.endswith("nate.com") or email.endswith("daum.net"):
#     print("가입 가능")
# else:
#     print("가입 불가능")      

# 문제 4. 금액 계산하기
# 각 업체별로 입금이 되었다. 총액이 얼마인지 출력 하세요
쿠팡 = "135,090원"
네이버 = "540,000원"
오드론 = "340,090원"

tot = int(쿠팡.replace(",","").replace("원","")) + int(네이버.replace(",","").replace("원","")) + int(오드론.replace(",","").replace("원",""))

print(f"합계 : {tot:,}원")
tot = tot.split("")
