







# name = input("이름 입력 : ").strip().lower()
# if name.__len__() >= 4 and name.__len__() <= 12 and name.isalnum():
#     print("사용 가능한 이름입니다.")
# else :
#     print("사용 불가능한 이름입니다. 이름은 4~12자 사이의 영문자와 숫자로만 구성되어야 합니다.")
# pw = input("비밀번호 입력 : ").strip()
# def mask_password(pw):
#     incode = pw[:2] + "*" * (len(pw) - 2)
#     return incode
# print(f"인코딩된 비밀번호 : {mask_password(pw)}")

emails = [
    "  Hong@NAVER.com  ",
    "kim@gmail.com",
    "lee@naver.com",
    "park@DAUM.NET",
    "choi@gmail.com  "
]
from collections import Counter
for i, email in enumerate(emails):
    email = email.strip().lower().split("@")
    
print(Counter(email[1]))