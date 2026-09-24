import numpy as np

arr = np.array([0,1,2,3,4,5,6,7,8,9])

print("Original array:", arr ,"\n")

modified_arr = []
for i in arr:
    if i%2 == 0:
        modified_arr.append(i)
    else:
        modified_arr.append(-1)

modified_arr = np.array(modified_arr)
print("Modified array by replacing odd numbers with -1: ",modified_arr,'\n')

twoD_arr = arr.reshape(2, 5)
print('2D version of original array: \n', twoD_arr,'\n')

total_sum = 0

for i in arr:
    total_sum += i

print("Total sum of original array: ", total_sum)