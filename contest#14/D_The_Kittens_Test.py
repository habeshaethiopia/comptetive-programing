from sys import stdin


def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
#topological sort

from collections import deque, defaultdict
def solve():
    
    n=int(input())
        
    root = [i for i in range(n)]
    ans= [ [i] for i in range(n)]
    
    def find(x):
        while x != root[x]:
            root[x] = root[root[x]]
            x = root[x]
        return x
    
    def union(x, y):
        rootX =  find(x)
        rootY =  find(y)
        if rootX != rootY:
            if  len(ans[rootX]) >  len(ans[rootY]):
                root[rootY] = rootX
                ans[rootX].extend(ans[rootY])

                # return [rootX]+ans[rootX]
                
            else:
                ans[rootY].extend(ans[rootX])
                root[rootX] = rootY
                # return [rootY]+ans[rootY]

              
    pr=[]    
    for _ in range(n-1):
        a,b=invr()
        pr=union(a-1,b-1)
    print(*list(map(lambda x:x+1, ans[find(0)])))




    
if __name__=='__main__':
    solve()