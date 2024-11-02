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
    m=[]
    for i in range(n):
        a=inlt()
        temp=max([a[i]-i+1 for i in range(1,a[0]+1)]) 
        m.append((temp, a[0]))
    


    m.sort()
    gain=[]
    x=0
    for i in m:
        gain.append(x)
        x+=i[1]
    
    ret=m[0][0]
    c=m[0][1]
    for i in range(1,n):
        ret+=max(0,m[i][0]-ret-gain[i])
        c+=m[i][1]
        # print(c,gain[i])/
    

    print(ret+1)
        
    
   
if __name__=='__main__':
    for _ in range(int(input())):
        solve()
