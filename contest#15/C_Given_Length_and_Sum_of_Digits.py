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
    
    m,s=invr()
    if 9*m<s or s<=0  and m>1:
        print(*[-1]*2)
    else:
        arr=[0]*m
        temp=s
        for i in range(m):
            if s-9>=0:
                s-=9
                arr[i]=9
            else:
                arr[i]=s
                break
        ans=[]
        s=temp
        ans.append(''.join(map(str, arr)))

        arr=[0]*m
        last=m-1
        for i in range(m-1,-1,-1):
            
            if s-9>=0:
                arr[i]=9
                s-=9
                last=i
                if s==0:
                    break
            else:
                arr[i]=s
                last=i
                # print(arr[i])
                
                break
        if arr[0]==0:
            arr[last]-=1
            # print(arr[m-i-1])
            arr[0]+=1
        # print(arr)
        ans.append(''.join(map(str, arr)))

        print(*ans[::-1])

    
if __name__=='__main__':
    solve()