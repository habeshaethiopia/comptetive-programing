# Problem: C - ANDy Session - https://codeforces.com/gym/522079/problem/C

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
    
    n,k=invr()
    a=inlt()
    arr=[0]*31
    for num in a:
        bit=bin(num)[2:]
        bit='0'*(31-len(bit))+bit
        # print(bit)
        for i in range(len(bit)):
            if bit[i]=='1':
                arr[i]+=1
    # print(arr)
    ans=''
    for i in range(len(arr)):
        if n-arr[i]<=k:
            # print(k,arr[i])
            ans+='1'
            k-=n-arr[i]
        else:
            ans+='0'
    # print(ans)
    print(int(ans,2))



if __name__=='__main__':
    for _ in range(int(input())):
        solve()