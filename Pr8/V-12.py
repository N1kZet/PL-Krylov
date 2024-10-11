print('№1')
from random import *
n = 3
arr = []
for i in range(n):
    a = []
    for j in range(n):
        a.append(randint(1,3))
    arr.append(a)
for i in arr:
    print(' '.join(list(map(str,i))))
print('-'*8)
res = []
for i in range(n):
    r = True
    for j in range(n):
        if arr[i][j] != arr[j][i]:
            r = False
            break
    if r:
        res.append(i)
print(res)
print('-'*8)
#---------------
print('№2')

n = 3
m = 4
arr2 = []
for _ in range(n):
    matrix = [randint(1,3) for a in range(m)]
    arr2.append(matrix)
'''
for i in range(n):
    a = []
    for j in range(m):
        a.append(randint(1,3))
    arr2.append(a)
'''
for i in arr2:
    print(' '.join(list(map(str,i))))

for i in range(n-1):
    for j in range(m):
        arr2[i][j] -=arr2[n-1][j]
print('-'*8)
for i in arr2:
    print(' '.join(list(map(str,i))))