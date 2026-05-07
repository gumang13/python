
import numpy as np
import matplotlib.pyplot as plt
# array = np.random.randint(50,100,(4,5))
# print(array.mean(axis=1))
# print(array.mean(axis=0))
# print(array.max())
# max_arr=array.max()
# print(np.argwhere(array == max_arr))

# arr = np.random.randint(1,50,20)
# print(arr[arr%2==0])
# print(arr[(arr>=10)&(arr<=30)])
# print(arr[(arr%5==0)&(arr>20)])

# arr = np.random.randint(50,100,(5,5))
# print(arr)
# avg = arr.mean(axis=1)
#
# print("평균점수 : ",avg)
#
# print(np.argwhere(avg<70).flatten())
# print(np.argwhere((avg>=75)&(avg<=85)).flatten())
# print(np.argwhere(arr.min(axis=1)>=70).flatten())
# print(np.argwhere(arr.mean(axis=0).min()==arr.mean(axis=0)).flatten())
# print(np.argwhere(arr>=80),np.bool(arr>=80).sum())
# sens = np.random.randint(0,101,(10,24))
# print(sens)
# avg = sens.mean(axis=1)
#
# print(avg)
# print((sens>=80).sum())

# 2026.05.07
# img = np.random.randint(0,256,(5,5))
# result=(100<=img)&(200>=img)
# print(f"{result.sum()}  {img[result].mean():.2f}")

img = np.random.randint(0, 256, (100, 100))

pos = np.argwhere(img <= 5)

min_row, min_col = pos.min(axis=0)
max_row, max_col = pos.max(axis=0)
cropped = img[min_row:max_row+1, min_col:max_col+1]

print("좌표 개수:", len(pos))
print("min(axis=0):", pos.min(axis=0))
print("max(axis=0):", pos.max(axis=0))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cropped, cmap='gray')
plt.title(f'cropped {cropped.shape}')
plt.axis('off')

plt.show()