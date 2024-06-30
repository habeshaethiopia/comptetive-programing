from sys import stdin
from math import ceil

def input():
    return stdin.readline().strip()


def inlt():
    return list(map(int, input().split()))


def insr():
    s = input()
    return list(s[: len(s) - 1])


def invr():
    return map(int, input().split())


def solve():
    n, h = invr()
    a=inlt()
    mn=ceil(h/n)
    add=0
    gap=[]
    for i in range(n-1):
        if a[i]+mn>a[i+1]:
            add+=a[i+1]-a[i]
        else:
            add+=mn
            g=a[i+1]-a[i]-mn
            gap.append(g)
    add+=mn
    if h <= add:
        print(mn)
    else:
        gap.sort()
        d=(h-add)/(len(gap)+1)
        l=d
        r=h-add
        temp=add
        ans=float('inf')
        while l<=r+1:
            mid=(l+r)//2
            for i in gap:
                if i>=mid:
                    temp+=mid
                else:
                    temp+=i
            
            if h>temp:
                l=mid+1
            else:
                ans=min(ans,mid)
                r=mid-1
        print(mn+ans)
        # print(gap, h-add)



if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
