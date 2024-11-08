#1
n = 3
m = 2
arr = []
file = open('data.txt')
for i in file.readlines():
    n1 = int(i)
    arr.append(n1)
arr = [arr]*n
for i in arr:
    print(' '.join(list(map(str,i))))

for i in range(n-1):
    for j in range(m):
        arr[i][j] -=arr[n-1][j]
print('-'*8)
for i in arr:
    print(' '.join(list(map(str,i))))
print('-'*8)
file_vivod = arr
print(file_vivod)
file_v = open('file_vivod.txt','w')
print(file_v.write(str(file_vivod)))
file_v.close()
for i in arr:
    print(*i)