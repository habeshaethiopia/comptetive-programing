from math import gcd
from collections import defaultdict
n=int(input())
a= list(map(int, input().split()))
b= list(map(int, input().split()))
mydic=defaultdict(int)
c=0
for i in range(n):
    if a[i]:
        if b[i]:
            if a[i]<0 and b[i]<0:
                a[i]*=-1
                b[i]*=-1
            elif a[i]<0 or b[i]<0:
                a[i]=-1*abs(a[i])
                b[i]=abs(b[i])
            g=gcd(a[i],b[i])
            mydic[(a[i]//g,b[i]//g)]+=1
        else:
            mydic[0]+=1
    elif a[i]==0 and b[i]==0 :
        c+=1
    
ans=0
# print(mydic)
for i in mydic:
    ans=max(ans, mydic[i])
print(ans+c)