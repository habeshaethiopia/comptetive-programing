from sys import stdin
from heapq import heapify, heappop,heappush,heappushpop, heapreplace

def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
def solve():
    
    n,k, q=invr()
    t=inlt()
    # t=[-i for i in t]
    # heapify(t)
    display=[]
    for i in range(q):
        typ, id =invr()
        # print(display)
        if len(display)<k and typ==1:
            heappush(display, (t[id-1],id))
        elif len(display)<=k and typ==1:
            if display[0][0]<t[id-1]:
                # heappop(display)
                heapreplace(display,(t[id-1],id))
        elif typ==2:
            if (t[id-1],id) in display:
                print('YES')
            else:
                print('NO')

if __name__=='__main__':
    solve()