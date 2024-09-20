a =input()
arr1 = [int(x) for x in a.split()]
arr2 = []
for  i in arr1:
    if i%2==1:
        arr2.append(i)
if len(arr2)>0:
    print(sorted(arr2,reverse=True))
else:
    print('Нет')