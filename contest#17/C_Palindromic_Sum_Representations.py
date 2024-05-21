from sys import stdin


def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
mod=10**9 +7
def coin(amount, coin):
    arr=[0]*(amount+1)
    arr[0]=1
    for c in coin:
        # if c > amount:
        #     break
        for i in range(amount):
            if i+c<=amount:
                arr[i+c]=(arr[i] + arr[i+c] )%mod
    return arr
def solve():
   
    arr=[]
    for i in range(1,40001):
        if str(i)[::-1]==str(i):
            arr.append(i)
    
    ans=coin(40000,arr)
    # print(len(arr),len( ans))

    for i in range(int(input())):
        n=int(input())
        

        print(ans[n])
    pass
if __name__=='__main__':
    solve()