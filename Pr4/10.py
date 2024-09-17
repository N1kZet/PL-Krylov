fib1 = 0
fib2 = 1

n = int(input('Номер элемента ряда Фибоначчи: '))
#Cколько надо добавить чисел к индексу
k = int(input('С какого элемента начинать: '))
#Индекс элемента
a = 0
res= 1
for i in range(k,k+n):
    while a < i:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        a += 1
        res+=fib_sum
print(res)
