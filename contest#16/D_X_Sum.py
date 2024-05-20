from sys import stdin


def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
def check(i,j):
    return i>=0 and j>=0 and i<n and j<m
    
def solve():
    n,m=invr()
    mtx=[]
    def check(i,j):
        return i>=0 and j>=0 and i<n and j<m
    l=[0]*(n+m)
    r=l[:]
    for i in range(n):
        row=inlt()
        mtx.append(row)
        for j in range(m):
            x=row[j]
            l[i-j+m-1]+=x
            r[i+j]+=x
    print(max(l[i-j+m-1]+r[i+j]-mtx[i][j] for i in range(n) for j in range(m)))
        
            
   
if __name__=='__main__':
    for _ in range(int(input())):
        solve()