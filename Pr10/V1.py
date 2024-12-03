#1
n = 4
a = []
with open("/home/n1kzet/PL-Krylov/Pr10/data.txt") as file:
    for line in file:
        arr = [int(x.strip()) for x in line.split()]
        a.append(arr)

print('Исходный массив:')
for i in a:
    print(*i)

for i in range(n-1):
    for j in range(n):
        a[i][j] -=a[n-1][j]

print('-'*8)
file_v = open('file_vivod.txt','w')
file_v.write(str(a))
file_v.close()
for i in a:
    print(*i)
