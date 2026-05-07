

# matplotlib : 그래프와 이미지를 눈으로 볼 수 있게 해주는 시각화 라이브러리 이다.


import numpy as np
import matplotlib.pyplot as plt

# x = [2023, 2024, 2025, 2026]
# y = [45, 34, 67, 51]
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False          # 마이너스 표시
# x = np.arange(0,10)
# tm = np.random.randint(1,10,10)
# y = tm*2
#
# plt.plot(x,y)   # x축, y축 그래프 그리기
#
# # plt.ylim(0,20) # y 축 값 범위 지정
# plt.yticks(range(0,21,1))        # y 축 범위 지정
# plt.xticks(range(10))
#
# plt.title("랜덤 숫자")
# plt.xlabel("count")
# plt.ylabel("number")
#
# plt.show()

x = ["자바", "스프링부트", "html", "데이터베이스", "파이썬", "css", "javascript", "진섭이는 게임을 못한다."]
y = [45, 56, 78, 91, 68, 77, 89, 10]
# plt.figure( figsize=(12,15) )  # 그래프 그리기 전에 크기 설정 ( 도화지 크기 )
plt.plot(x,y)
plt.xticks(rotation=45)        # 글자 길어서 겹치면 돌려주기
# plt.tight_layout()             # 그래브 여백 자동 설정
plt.subplots_adjust(bottom=0.3)  # 그래브 여백 (top, bottom, right,left) 설정
# dpi 저화질 - 72 , 고화질 - 300, 중간 - 150      웹에는 저화질이 좋다
# transparent = True    >>> 배경 투명하게 png파일만 가능
plt.savefig("test.png",dpi=300, transparent=True )          # 그래프 저장하기

plt.show()