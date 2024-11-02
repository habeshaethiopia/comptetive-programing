from sys import stdin
from collections import Counter

def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))
def solve():
    n=int(input())
    a=inlt()
    a.sort(reverse=True)
    odd=[i for i in a if i%2]
    even=[i for i in a if i%2==0]
    al=0
    bo=0
    for i in range(n):
        if a[i]%2 and i%2:
            bo+=a[i]
        elif a[i]%2==0 and i%2==0 :
            al+=a[i]


    # print(bo,al)
    if al>bo:
        print("Alice")
    elif bo>al:
        print("Bob")
    else:
        print("Tie")
if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
