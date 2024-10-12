#1
from random import *
n = 3
m = 2
arr = []
for _ in range(n):
    matrix = [randint(1,3) for a in range(n)]
    arr.append(matrix)

for _ in arr:
    print('-'.join(list(map(str, _))))
max_arr = arr[0][0]
max_index = 0
for i in range(n):
    if max_arr<arr[i][i]:
        max_index = i
        max_arr = arr[i][i]
def swap(arr,row1,row2):
    arr[row1],arr[row2] = arr[row2],arr[row1]
swap(arr,max_index,m)

print('-'*8)

for i in arr:
    print(*i)