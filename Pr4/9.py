fib1 = 0
fib2 = 1

n = int(input('Номер элемента ряда Фибоначчи: '))
res = 1
i = 0
while i < n:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i += 1
    res += fib_sum
print('Сумма элементов:', res)
