

import matplotlib.pyplot as plt
import numpy as np


# img = np.array([
#     [0,50,100],
#     [150,200,255]
# ])
img = np.random.randint(0,256,(100,100))

bright = np.clip(img+50,0,255)

copy_img = img.copy() # 원본 복사
copy_img[ copy_img>=128 ] = 255
copy_img[ copy_img<128 ] = 0

plt.figure( figsize=(8,4) )

plt.subplot(1,2,1)   # 1,2,1  > 1행 2열 첫번째칸에 배치

plt.imshow(copy_img, cmap='gray')
plt.title('copy')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(img, cmap='gray')
plt.title('original')
plt.axis('off')

plt.show()