

import numpy as np

img = np.array( [
    [10, 20, 30],
    [40, 50, 60]
])

v = np.array( [10, 20, 30] )

print( img + v )

# 열방향 브로드 캐스팅
v2 = np.array( [[100], [200]]) # 2차원 배열
print( img + v2 )

# 2행 3열 + 1차원 (데이터 3개)
# 2행 3열 + 2차원 (2행 1열)
# (5,4,3) + (3, )