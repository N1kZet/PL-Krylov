s = input()
stroka = s.split()
for i in stroka:
    if i.endswith('я') or i.startswith('а'):
        print(i)