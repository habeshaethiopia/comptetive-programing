from sys import stdin


def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
def solve():
    n,q=invr()
    
    parent = {i:i for i in range(1, n+1) }
    size = [1] * (n+1)
    
    type2={i:i+1 for i in range(1, n+1)}
    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        parentX = find(x)
        parentY = find(y)
        if parentX != parentY:
             if size[parentX] > size[parentY]:
                 parent[parentY] = parentX
                 size[parentX] += size[parentY]
             else:
                 parent[parentX] = parentY
                 size[parentY] += size[parentX]
    for _ in range(q):
        
        t,x,y =invr()
        if t==3:
            if find(x)==find(y):
                print('YES')
            else:
                print('NO')
        elif t==1:
            union(x,y)

        else:
            new_dep=type2[x]
            while new_dep <=y:
                union(new_dep,x)
                temp=type2[new_dep]
                type2[new_dep]=type2[y]
                new_dep=temp

               
    
if __name__=='__main__':
    solve()