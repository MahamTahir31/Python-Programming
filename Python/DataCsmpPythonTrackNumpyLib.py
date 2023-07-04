# python's numpy library :

import numpy as np

# 1D Numpy Arrays
# _______________

l1 = [1,2,3,4]
arr1=np.array(l1)
print("1D array : \n",arr1)
l2 = [1,2,3,4]
arr2 = np.array(l2)
print("sum of each element in an array : \n",arr1+arr2)

a= np.round(1.54)
print(a)

# BODY MASS INDEX (BMI)
weight = [1.2,2.4,2.2]
height = [2.3,6.7,1.5]
w = np.array(weight)
h = np.array(height)
bmi = w/h**2
print(bmi)
print(bmi[1])
print(bmi>0.1)
print(bmi[bmi>0.1])
print(type(bmi))

# 2D Numpy Arrays
# _______________

TD = np.array([[1,2,3],[2,4,5]])
print("2D array : \n",TD)
print(TD.shape) # 2 rows, 3 columns
print(TD[0,2])
print(TD[0][2])
print(TD[:,0:2])
print(TD[1,:])

# Statistical methods via Numpy
# _____________________________

mean = np.mean(TD[:,0])
median = np.median(TD[:,0])
corr = np.corrcoef(TD[:,0],TD[:,1])
stand = np.std(TD[:0])
print(mean)
print(median)
print(corr)
print(stand)














