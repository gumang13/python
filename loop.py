

# for i in range(22,29):
#     print("숫자: "+str(i))

# for ch in "hello":
#     print(ch)

# for name in ["차도헌","박지연","이성찬","김진숙","이동렬","김현규"]:
#    if name.startswith("이"):
#          print(name)

# # 문제 1 . 1부터 10까지의 총 합을 구하세요

# total = 0 
# for i in range(1,11):
#     total += i
# print(total)

# word = "hello"
# for i in range(len(word)-1,-1,-1):
#     print(word[i])

# word = "level"
# reword =word[::-1]

# if word == reword:
#     print("회문입니다")
# else:    print("회문이 아닙니다")

# 문제 2 . [ "15,000","13,000","8,700","9,000","25,000"]
# 배열에 출금 금액들이 저장되어 있다.
# 만원 이상 금액들에 대해서 출력.
# money = [ "15,000","13,000","8,700","9,000","25,000"]
# # result = ""
# # for m in money:
# #     result = m.replace(",","") 
# #     if int(result) >= 10000:
# #         print(m)
# # word = "hello world"
# # count= 0
# # for ch in word:
# #     if ch in "a" or ch in "e" or ch in "i" or ch in "o" or ch in "u":
# #         count += 1
# #         print(ch)
# # print("모음의 개수 : "+str(count))

# text = "banana"
# count = {}
# for ch in text:
#     if ch in count:
#             count[ch] += 1
#     else:
#             count[ch] = 1
# print(count)

# # for i in range( len(money) ):
# #        print(i, money[i])
# for i,v in enumerate(money):
#        print(i,v)

# # 문제 3 . [89, 56, 78, 92, 61, 96, 83, 74]
# # 203호 학생들의 성적이다. 성적의 총합과 평균을 출력하세요
# scores = [89, 56, 78, 92, 61, 96, 83, 74]
# total = 0 
# avg = 0 
# for i,s in enumerate(scores):
#        total += s
#        avg = total / len(scores)
#        if s >= 80:
#               print(f"80점 이상인 인덱스 : {i}  점수 : {s}")
# print(f" 총합 : {total}, 평균 : {avg:.2f}")

# 반복문 while

# while 조건:
#        실행코드

# while 문은 조건식이 참인 경우에 동작 하기 때문에 
# 쉽게 무한 루프에 들어 갈 수 있다.
# 하여 while문 사용시 중단 시킬 수 있는 break를 같이 사용하는게 좋다.
# num = 5 
# while num > 2:
#        print("2보다 크다")
#        break

# while True:
#        cmd = input("명령어 입력 : ").strip().lower()
#        if cmd == "history":
#               print("명령어 기록") 
#        elif cmd == "mkdir"  :
#               print("폴더 생성")
#        elif cmd == "remove":
#               print("파일 삭제")
#        elif cmd == "exit":
#               print("프로그램 종료")
#               break
#        else:
#               print("알 수 없는 명령어입니다.")

import random
# while True:
#  num = random.randint(1,10)
#  word = input("앞 or 뒤 선택 : ").strip().lower()
#  if word == "앞"or word == "뒤":
#     if num <= 5 and word == "앞":
#         print("맞췄습니다")
#         break
#     elif num > 5 and word == "뒤":
#         print("맞췄습니다")
#         break
#     else:
#         print("틀렸습니다")
        
#  else:
#        print("잘못된 입력입니다. '앞' 또는 '뒤'를 입력해주세요.")

n = random.randrange (1,10) # 1~9

game = ["가위","바위","보"]
com= random.choice(game)
# print(n) # 0~2
print(f"컴퓨터 : {com}")
num = 0
# while True:
#        user = input("1. 가위 2. 바위 3. 보 : ").strip()
#        if user in ["1","2","3"]:
#               user = int(user) - 1
#               print(f"사용자 : {game[user]}, 컴퓨터 : {n}")
#               if user == 0 and n == "가위" or user == 1 and n == "바위" or user == 2 and n == "보":
#                      print("비겼습니다")
#               elif user == 0 and n == "보" or user == 1 and n == "가위" or user == 2 and n == "바위":
#                      print("이겼습니다")
#               else:
#                      print("졌습니다")
              
#        else:
#               print("잘못된 입력입니다. '1', '2', '3' 중 하나를 입력해주세요.")
#        num += 1
#        if num == 5:
#               print("게임 종료")
#               break
       
# 0
user = input("1. 가위 2. 바위 3. 보 : ").strip()
cidx = game.index(com)
uidx = game.index(user)

comp = cidx - uidx

if com == user:
    print("비겼습니다")
elif comp == -1 or comp == -2:
       print("이겼습니다")
else:
       print("졌습니다")