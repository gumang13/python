
import numpy as np

img = np.array([
    [10, 20, 30, 40, 50],
    [60, 200, 210, 70, 80],
    [90, 220, 255, 100, 110],
    [120, 130, 140, 150, 160]
])

print(img>=200)

# 밝은 영역을 더 밝게
copy_img = img.copy()   # 원본 데이터 유지를 위한 복사
copy_img[copy_img>=200] = 255
print(copy_img)

# 밝은 영역이 몇군데 ??
count = np.sum( copy_img == 255 )
print(count)
# 밝은 영역 좌표는 ??
pos = np.argwhere(copy_img == 255)
print("좌표는?",pos)

# 밝은 영역 위치의 값만 추출하기
rows = pos[:,0]
cols = pos[:,1]
print("행 : ",rows)
print("열 : ",cols)

min_row = rows.min()    # 행번호의 최솟값
max_row = rows.max()    # 행번호의 쵀댓값
min_cols = cols.min()   # 열번호의 최솟값
max_cols = cols.max()   # 열번호의 최댓값
# img[1:2, 1:2]
find = img[min_row : max_row+1, min_cols : max_cols+1]
print( find )