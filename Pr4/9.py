fib1 = 0
fib2 = 1

n = int(input('Номер элемента ряда Фибоначчи: '))

i = 0
while i < n - 1:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1

print('Значение этого элемента:', fib2)
