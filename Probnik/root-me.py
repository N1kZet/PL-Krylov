from sys import *
setrecursionlimit(30000)
def f(u):
    if u==0:
        return -47
    elif u!=0:
        return -31 + f(u) - u*38
print(f(10))
