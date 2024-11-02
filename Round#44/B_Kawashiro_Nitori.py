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
    n,k=invr()
    s=input()
    for i in range(n-2*k):
        print(s[i:k+i],s[i+k+1:i+2*k+1],"***")
        if s[i:i+k]==s[i+k+1:i+2*k+1]:
            print("YES")
            break
    else:
        print("NO")
if __name__=='__main__':
    for i in range(int(input())):
        solve()