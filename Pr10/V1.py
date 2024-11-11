#1
n = 4
arr = []
#Заполняем массив элементами из файла data.txt
file = open('data.txt')
for i in file.readlines():
    n1 = int(i)
    arr.append(n1)
arr = [arr]*n
for i in arr:
    print(*i)
max_e = -float('inf')
min_e = +float('inf')
max_index = [0,0]
min_index = [0,0]
#Нахождение max и min числа и индекса
for i in range(n):
    for j in range(n):
        if arr[i][j]>max_e:
            max_e=arr[i][j]
            max_index = ([i,j])
        if arr[i][j]<min_e:
            min_e = arr[i][j]
            min_index = ([i,j])
#Замена max и min индекса
row1,row2 = max_index[0],max_index[1]
row3,row4 = min_index[0],min_index[1]
arr[row1][row2],arr[row3][row4]=arr[row3][row4],arr[row1][row2]
#print(max_e,max_index)
#print(min_e,min_index)
print('-'*8)
#Добавляем результат в файл file_vivod.txt
file_vivod = arr
#print(file_vivod)
file_v = open('file_vivod.txt','w')
#print(file_v.write(str(file_vivod)))
file_v.close()
for i in arr:
    print(*i)