def prosto(n, divisor):
  if n <= 1:
    return False
  if divisor * divisor > n:
    return True
  if n % divisor == 0:
    return False
  return prosto(n, divisor + 1)

n = int(input("Введите натуральное число n>1: "))

if prosto(n, 2):
  print("YES")
else:
  print("NO")