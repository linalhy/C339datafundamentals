adj = ["red", "big", "yummy"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x,y)

for i in range(1, 11):
    for j in range(1, 11): # iterate from 1 to 10
         print(i * j, end=' ') # print multiplication
    print(f": ", {i}, "times tables")

num = 21
counter = 1
print(f"The multiplication table of {num}")
while counter <= 10:
        ans = num * counter
        print (num, 'x', counter, '=', ans)
        counter = counter + 1

another_list2 = []
term2 = [3, 5, 1, 4, 6]
while another_list2:
    term2.append((another_list2.push()) ** 2)
print(term2)

list5 = [1, 2, 3, 4, 5, 6 , 7, 8, 9]
prefixArray = [0] * len(list5)
prefixArray[0] = list5[0]
for i in range(1, len(list5)):
    prefixArray[i] = prefixArray[i-1] + list5[i]
print(prefixArray)

def sum(startIndex, endIndex):
    if startIndex == 0:
        return prefixArray[endIndex]
    return prefixArray[endIndex] - prefixArray[startIndex - 1]

print(sum(3,5))

import time
import numpy as np

list5 = [1, 2, 3, 4, 5, 6 , 7, 8, 9]
print("list5 :", list5)

loop_num = 10000
range_sum = [3,5]

startTime = time.time()
prefixArray = [0] * len(list5)
prefixArray[0] = list5[0]

# Calculating the running sums into prefixArray
for i in range(1, len(list5)):
    prefixArray[i] = prefixArray[i-1] + list5[i]
print("prefixArray: ", prefixArray)

# We can also simply use the cumsum function in numpy to calculate the running sums:
prefixArray = np.cumsum(list5)
print(prefixArray)

def sumAll(startIndex, endIndex, prefixArray):
    return prefixArray[endIndex] - prefixArray[startIndex - 1]
for i in range(0,loop_num):
    a = sumAll(range_sum[0], range_sum[1], prefixArray)
print(f'First Method took {time.time() - startTime} s')

# Simpler method (readable) and faster when lower ranged sums are made 
start_time = time.time()
for i in range(0,loop_num):
    a = sum(list5[range_sum[0]:range_sum[1]+1]) 
print(f'Second Method took {time.time() - start_time} s')
