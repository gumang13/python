# 리스트 , 튜플
# 리스트 - 여러 데이터를 저장 관리 하기 위한 파이썬 자료 구조 이다.
# 튜플도 리스트와 같은데 차이점은 리스트는 수정이 가능하지만 튜플은 수정 x 

#리스트 - 순서 유지 , 인덱스를 통해 접근 , 추가 , 수정 , 삭제 가능
# 다른 자료형도 저장 가능 
# number = [10,20,30,40,50]
# empty = []
# name = list()

# # print( number[3] )

# #리스트 자르기
# num = number[2:4]
# print(num)
# num2 = number[:3]
# print(num2)

# # 리스트 수정 
# number[2]=100
# print(number)

# # 리스트 추가
# number.append(60) # 맨 뒤에 추가 
# print(number)
# number.insert(2, 500) # 원하는 위치에 추가
# print(number)

# # 리스트 값 삭제
# number.remove(100) # 리스트에서 삭제 할 데이터 입력
# print( number )
# number.pop(1) # 인덱스 입력
# print( number )
# del number[2] # 인덱스 입력
# print( number )

# print( len(number) ) # 리스트 길이

# for num in number:
#     print( num )

# for i , num in enumerate(number):
#     print( f"{i} : {num}" ) 

# # 리스트 검색
# print( 50 in number ) # 리스트 안에 존재여부 (True/False)
# print( number.index(50) ) # 리스트 안에 존재하는 데이터의 인덱스 반환 (존재하지 않으면 에러)
# # index를 통해 인덱스를 찾기 전에 in으로 존재여부 확인 먼저 하기

# #리스트 정렬 
# number.sort() # 오름차순 정렬
# print( number )
# number.sort(reverse=True) # 내림차순 정렬
# print( number )
# #리스트 는 일반적으로 많이 사용되는 자료구조이다.
# #자바에서 list (Arrylist)를 많이 사용 된다면 파이썬은 리스트 이다.
# # 여러 데이터를 저장 할 수 있고, 수정 ,추가 가능하고 반복문 사용 쉽고
# #정렬, 검색도 되고 그래서 사용하기 좋다

# #리스트 문제 풀기
# # 문제 1. 5명의 이름이 저장되어 있는 리스트 만들기
# # 5명의 이름 출력하는 반복문 만들기

# name=["홍길동", "김철수", "이영희", "박영수", "최민수"]
# for n in name:
#     print(n,end=" ")
# name.append("정도전")
# for n in name:
#     print(n,end=" ")
# print()
# # 문제 3. 리스트에 김유신이 있는지 확인하는 코드 작성하기
# if "김철수" in name:
#     print(name.index("김철수"))
# #문제 4 . 이름 리스트에 내림차순으로 정렬 
# name.sort(reverse=True)
# print(name)

# # 문제 5. 
# fruits = ["사과", "바나나", "파인애플", "딸기", "오렌지", "포도", "배"]
# fruit = [x for x in fruits if len(x) == 2]
# fruits.sort(key=len)
# print(fruit)

# # 문제 6. 과일 검색 프로그램 만들기
# # 과일이름 키보드를 통해 입력받는다.


# # fruit = [x for x in fruits if x==user]
# # if fruit!=[]:
# #    print(f"{fruit}판매중")
# # else:
# #     print("품절")
# fruits.sort() # 딸기 , 바나나 , 배 , 사과 , 오렌지 , 파인애플 , 포도 
# price = [5000,8000,12000,9500,15500,20400,9000]
# tot=0
# while True:
#   user=input("과일 이름 입력 or 0번입력(종료): ")
#   if user in fruits:
#      tot+= price[fruits.index(user)]
#      print(f"{user}이(가) 추가 되었습니다.")
#   elif user==0 or user=="0":
#       break
#   else:
#       print("잘못된 입력 입니다")

# print(f"지불 해야 할 총 금액 : {tot}")

# 튜플 - 리스트처럼 여러 데이털르 저장 할수 있는 자료형이다.
#  저장한 데이터를 수정 할 수 없다.
# 데이터를 보호 하기 위한 목적
# 속도와 메모리 효율 성 
# 딕셔너리의 키로 사용 
# 여러개의 값을 반환(return) 시킬때

# 튜플 만들기 
number = (10,20,30,40) # 작은괄호 - 튜플 , 대괄호 - 리스트 
print(number)
print( type((1,2,3,4)))
print(type((10,)))

print(number[1])  # 인덱스 0 부터 시작

# 튜플 슬라이스 ( 자르기 )
print(number[1:3])

# 튜플 검색
print( 10 in number)
print( number.index(20))

# 리스트와 다른점
# 수정 불가
# number.append(200) 오류 -> 추가도 안됨
# number.remove(20)  삭제도 안됨
# number.pop(20)  이것도 오류
# del number[2]  이것도 오류

print( number.count(20) ) # 특정 값 갯수 구하기 

data = 10,20,30,40,50   # 패킹 - 여러값을 하나로 묶기
print(type(data))

a,b,c,d,e= data
print(a,b,c,d,e)

red = 20
blue = 10
red,blue = blue,red
print(red,blue)

# 리스트 <--> 튜플 
info = ("다음주","금요일","빨간날","그래서","우리는","5월6일에","봐요")
info_list=list(info)
info_list[0]="이번주"

info =tuple(info_list)
print(info)