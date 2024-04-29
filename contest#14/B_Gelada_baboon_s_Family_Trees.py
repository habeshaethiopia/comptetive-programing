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


def solve():
    n=int(input())
    p=inlt()
    root = {i:i for i in range(n+1)}
    size = [1] * (n+1)
    def find(x):
        while x != root[x]:
            root[x] = root[root[x]]
            x = root[x]
        return x

    def union(x, y):
        rootX =  find(x)
        rootY =  find(y)
        if rootX != rootY:
            if  size[rootX] >  size[rootY]:
                root[rootY] = rootX
                size[rootX] +=  size[rootY]
            else:
                root[rootX] = rootY
                size[rootY] +=  size[rootX]
        

    for i in range(1,n+1):
        union(i,p[i-1])
    ans=0   
    for i in range(1,n+1):
        if root[i]==i:
            ans+=1
    print(ans)
        
    
    
    

if __name__=='__main__':
    solve()