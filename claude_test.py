
import numpy as np

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
sens = np.random.randint(0,101,(10,24))
print(sens)
avg = sens.mean(axis=1)

print(avg)
print((sens>=80).sum())