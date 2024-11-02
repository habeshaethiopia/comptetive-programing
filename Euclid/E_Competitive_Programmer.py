from sys import stdin
from collections import Counter
from math import gcd


def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))
def solve():
    n= input()

    flag=True
    for i in n:
        if i =='0':
            n=n.replace("0","",1)
            # print(n)
            break
    else:
        flag=False
    for i in n:
        if int(i)%2==0:
            break
    else:
        flag=False
    x=0
    for i in n:
        x+= int(i)
    if x%3:
        flag=False
    
    if flag :
        print("red")
    else:
        print("cyan")
    
if __name__=='__main__':
    for _ in range(int(input())):
        solve()