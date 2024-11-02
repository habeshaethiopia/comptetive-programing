from sys import stdin
from collections import Counter, defaultdict,deque


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
    p=inlt()
    tree=defaultdict(list)
    child={}
    for i in range(n-1):
        tree[p[i]-1].append(i+1)
        child[i+1] = p[i]-1
    print(tree)
    add={}
    # while len(tree)>3:
    for i in range(n):
        if i not in tree:
            if child[i] in add:
                add[child[i]]=min(a[i], add[i])
                a[i]=0
            else:
                child[i]=a[i]
    for i in add:
        a[i]+=add[i]
        del tree[i]

    print(tree, "==", a)



if __name__=='__main__':
    for _ in range(int(input())):
        solve()