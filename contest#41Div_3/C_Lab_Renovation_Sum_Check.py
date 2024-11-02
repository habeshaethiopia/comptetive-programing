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
    mtx=[]
    for i in range(n):
        r=inlt()
        mtx.append(r)
    coll=[[]for i in range(n)]*n
    for i in range(n):
        for j in range(n):
            coll[j].append(mtx[i][j])
    valid="Yes"
    for i in range(n):
        for j in range(n):
            if mtx[i][j] != 1:
                for num in mtx[i]:
                    if mtx[i][j]-num in coll[j]:
                        break
                else:
                    valid="No"
        if valid=="No":
            break
    print(valid)
    
if __name__=='__main__':
    solve()