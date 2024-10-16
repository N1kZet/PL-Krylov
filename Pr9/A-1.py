from math import *
print('№1')
def f(x,n):
    return (x**n)/factorial(n)
a = int(input())
b = int(input())
print(f(a,b))
print('-'*6)
print('№3')
def f(n):
    a = n[::-1]
    return a
print(f(input()))