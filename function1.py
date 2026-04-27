

# 제어자 반환타입 메서드 이름 ( 매개변수 )

# 파이썬 함수 - def 함수이름 ( 매개변수 ):

# def hi():
#     print("안녕")

# # 함수 실행 - 호출
# # 함수이름() - () 소괄호에 매개변수가 있다면 넣어주기

# hi()

# def intro(name : str):
#     print( name , "님 로그인 하였습니다.")
# name="김유신"
# if type(name) == str : # isinstance ( name , str )
#     intro(name)
# ref=["ad","dd"]
# intro("김유신")
# intro(ref)

# def dataInput(a,b,c):
#     print(a + b + c)

# dataInput(1,20,30)

# # 함수를 만들때(정의) 어떤 기능을 가진 함수를 만들것인가
# # 해당 기능이 작동되기 위해서 필요한 것이 무엇인가.
# # 필요한 것들이 함수 안에서 만들 수 있는 것인가 아니면 외부에서 받아야 하는 것인가.

# # 함수의 반환값 return - 함수가 호출 된 위치로 돌려보내는 작업, 그리고 함수의 종료

# def add(num1,num2):
#     return "계산결과",num1+num2

# comment,res = add(10,20)
# print(comment,res)

# 변수의 범위 - 지역변수 ,전역변수
# number = 1000

# def totalPrice( price ):
#     total = 0
#     for money in price:
#         total += money
#     global number 
#     number = total         # 전역변수의 수정은 안된다. global을 붙여줘야 수정 가능 


# totalPrice( [ 1,2,3,4,5 ])
# print( number )
  

#문제 1. 간단한 함수 만들기.
# 사각형의 너비와 높이를 받아서 넓이를 출력하는 함수를 만들어 호출 해보세요

# def area(w,h):
    
#     return  w*h

# print(area(3,4))

# 문제 2 . 아래 코드를 보고 함수를 만드세요
# 로그인 체크 함수 만들기

# id = input("아이디를 입력하세요 : ")
# pw = input("비밀번호를 입력하세요 : ")



# def login(id,pw):
#     if id=="admin" and pw=="1234":
#      print("로그인 성공 하였습니다")
#     else:
#      print("아이디 또는 비밀번호를 잘못 입력했습니다.")

# login(id,pw)

# 문제3. 상품의 재고를 확인하여 재고 충분, 재고 부족, 품절 이라고 출력 할 수 있는 함수 만들기
# 재고 부족 기준은 현재 재고량이 8 이하인 경우

# def amount(num : int):
#     result =""
#     if num<=8:
#         result = "재고 부족"
#     elif num==0:
#        result = "품절!!!!!!!!!!"
#     else:
#        result = "재고 충분!!!"
#     return result
# print(amount(87))

# 문제4. 회원가입을 한다. 아이디 중복 체크 함수를 만드세요

id_list=["kim","lee","sky","gold","war123","qwer12","eeee14"]
#id_list 는 현재 가입된 회원들의 아이디만 저장된 리스트이다.
# 아이디 중복 체크 함수를 통해 사용가능,불가능 여부를 출력

def check_id(id):
    if id in id_list:
        print("사용 불가능! 이미 있는 아이디 이름 입니다")
    else:
        print("사용 가능한 아이디 입니다")

