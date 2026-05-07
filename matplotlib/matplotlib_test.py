
'''
    125번 png와 json 파일을 사용하여 다음을 만들어 보세요

    이미지 안에서 차량의 크기가 가장 큰 차와
    크기가 세번째로 큰 차를 바운딩 박스로 표시해 주세요
    가장 큰 차의 바운딩 박스 테두리 색은 red
    세번째로 큰 차의 바운딩 박스 테두리 색은 yellow

'''
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import json
import matplotlib.patches as patches
pos = list()
with open('18396708_frame_125.json','r',encoding='utf-8') as f:
    data = json.load(f)

for ann in data['frames']['annotations']:
    # vehicle = ann['category']['code']
    # area = ann['label']['width']*ann['label']['height']
    # if vehicle!='vehicle':
    #     continue
    label=ann['label']
    pos.append( (label['x'],label['y'],label['width'],label['height'] ) )
pos = sorted(pos,key=lambda x:x[2]*x[3],reverse=True)
pos = pos[0:3:2]
img=plt.imread('18396708_frame_125.png')
plt.imshow(img)
print(pos)
ax = plt.gca()
for (x,y,w,h) in pos:
    color = ('red' if pos[0][0]==x else 'yellow')
    # if pos[0][0]== x:
    #     color='red'
    # else:
    #     color='yellow'
    box = patches.Rectangle(
        (x, y),  # 시작 좌표
        w,  # 너비 크기
         h,  # 높이 크기
        fill=False,  # 박스 내부 색 채우기 여부
        edgecolor=color,  # 박스 테두리 색
        linewidth=2  # 테두리 선 굵기
    )
    ax.add_patch(box)
plt.show()