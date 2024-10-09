a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
if a<b:
    while a<=b:
        print(a)
        a+=1
else:
    while a>=b:
        print(a)
        a-=1
