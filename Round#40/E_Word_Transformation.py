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
    s,t=input().split()
    t=t[::-1]
    s=s[::-1]
    last=set()
    l=0
    for i in range(len(t)):

        for j in range(len(s)):
            if t[i]==s[j] and j not in last:
                
                last.add(j)
                break
        else:
            print("NO")
            break
        if l>j:
            print("NO")
            break
        l=j
    else:
        print("YES")
   
if __name__=='__main__':
    for _ in range(int(input())):
        solve()