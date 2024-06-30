from sys import stdin


def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:]))
def invr():
    return(map(int,input().split()))
def solve():
    for _ in range(int(input())):
        n,k=invr()
        s=insr()
        c=0
        l=0
        r=n-1
        # while l<r:
            
        #     if s[l]!=s[r]:
        #         s[r]=s[l]
        #         # c+=1
        #     l+=1
        #     r-=1
        
        for m in range(n//k-1):
            for i in range(m*k,(m+1)*k):
                # print(i,i+k,(m+1)*k)
                if s[i] != s[i+k] :
                    c+=1
                    s[i]=s[i+k]
        print(c)
        print(s==s[::-1])
    pass
if __name__=='__main__':
    solve()