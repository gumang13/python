
import numpy as np

# 2차원 배열
#[ [1, 2, 3], [4, 5, 6] ]

arr = np.array( [
    [1, 2, 3],
    [4, 5, 6]
] ) # numpy 2차원 배열은 2차원 리스트를 통해 만든다.
print( arr )
arr[0][0] = 100
print( arr.shape )

print( arr[1][0])
print( arr[1]) # 행 전체
print( arr[:,1]) # 모든 행에서 2열 값 가져오기
print( arr[0,1]) # arr[0][1]
arr[0][1] = 400
print( arr )
arr[0,1] = 500
print( arr )
print( arr[1]+100 )

# 배열 정보 확인
# arr.dtype : 데이터 타입
# arr.size : 총 데이터 개수
# arr.shape : 배열의 모양 ( 차원과 갯수 )
# arr.ndim : 배열의 차원수

# 문제 1.
scores = np.array( [
    [90, 89, 78],
    [94, 74, 56],
    [75, 68, 81]
])

# scores은 몇차원 이고 총 데이터 갯수는 ?
# 2행의 총 합은 ?
# 3열 전체를 출력
# scores 전체 평균값은 ?
# 2열의 평균은 ?
print(scores.ndim,scores.size)
print(scores[1].sum())
print(scores[:,2])
print(f"{scores.mean():.2f}")
print(scores[:,1].mean())