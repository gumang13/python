#  pandas_json.py

import pandas as pd
import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches

with open("012_000000.json", "r", encoding="utf-8") as f:
    data = json.load(f)

annotations = [
    a for a in data["annotations"]
    if "category_name" in a
]
# 데이터프레임 으로 저장하기
df = pd.DataFrame(annotations)
counts = df['category_name'].value_counts()
print("트럭 : " , counts['truck'] )

# 차량들의  너비 값 출력
car_width = df["bbox"].apply(lambda x : x[1][0])
print(car_width)


#  문제  너비가  가장 큰 차량을 찾으시오, 이미지에 바운딩박스표시하기
max_width = df["bbox"].apply(lambda x : x[1][0]).idxmax()
bbox = df.loc[max_width,"bbox"]
x,y = bbox[0]
w,h = bbox[1]

img=plt.imread('012_000000.jpg')
plt.imshow(img)

ax = plt.gca()
box = patches.Rectangle(
        (x, y),  # 시작 좌표
        w,  # 너비 크기
         h,  # 높이 크기
        fill=False,  # 박스 내부 색 채우기 여부
        edgecolor='red',  # 박스 테두리 색
        linewidth=2  # 테두리 선 굵기
    )
ax.add_patch(box)
plt.show()


#  문제  각 차량별 너비를 구하여  그래프로 출력해보세요

result = df.groupby("bbox")

result.plot(kind='bar')
plt.show()