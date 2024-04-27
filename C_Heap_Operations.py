from sys import stdin
from heapq import  heapify, heappop, heappush,nsmallest


def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

def solve():
    n=int(input())
    flag=True
    arr=[]
    ans=[]
    heapify(arr)
    for i in range(n):
        com=input().split()
        num=int(com[1]) if len(com)>1 else 0
        com=com[0]
        if com== 'insert':
            ans.append(f'insert {num}')
            heappush(arr,num)
        elif com== 'getMin':
            while arr and arr[0]<num:
                # print(nsmallest(1,arr))
                ans.append('removeMin')
                heappop(arr)
            if not arr or arr[0] > num:
                ans.append(f'insert {num}')
                heappush(arr,num)
            ans.append(f'{com} {num}')
        else:
            if arr:
                ans.append('removeMin')
                heappop(arr)
            else:
                ans.append('insert 0')
                ans.append('removeMin')
            
    print(len(ans))
    print(*ans , sep='\n')


    
if __name__=='__main__':
    solve()