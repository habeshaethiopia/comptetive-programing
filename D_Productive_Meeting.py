from sys import stdin
from heapq import heapify, heappop, heappush


def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
def solve():
    for _ in range(int(input())):
        n=int(input())
        idx=0
        a=[]
        for i in inlt():
            idx +=1
            a.append((-i,idx))
        
        
        heapify(a)
        ans=0
        idxs=[]
        while len(a)>1:
            x,ix=heappop(a)
            y,iy=heappop(a)
            if x<0 and y<0:
                ans+=1
                x+=1
                y+=1
                # print(x,y)
                idxs.append([ix,iy])
                
                if x<0 :
                    heappush(a,(x,ix))
                if y<0 :
                    heappush(a,(y,iy))
            
        print(ans)
        for i in idxs:
            print(*i)

        
    
if __name__=='__main__':
    solve() 