#1
arr = [int(x) for x in (input('Введите числа массива: ')).split()]
max = -float('inf')
for i in arr:
    if i>max:
        max=i
print(max)
print('-'*8)
#2
arr_A = [0,1,2,3,4,5,6,7,8,9]
arr_B = [10,11,12,13,14,15,16,17,18,19]
# Обмен содержимым массивов A и B
arr_A, arr_B = arr_B, arr_A

# Вывод преобразованных массивов
print("Массив A:", arr_A)
print("Массив B:", arr_B)
