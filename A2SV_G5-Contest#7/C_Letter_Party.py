n,k=map(int,input().split())
s=input()
l=0
ans1=0
temp=k
for i in range(n):
    if s[i]=='b':
        k-=1
    while k<0:
        if s[l]=='b':
            k+=1
        l+=1
    ans1=max(ans1,i-l+1)
ans2=0
l=0
k=temp
for i in range(n):
    if s[i]=='a':
        k-=1
    while k<0:
        if s[l]=='a':
            k+=1
        l+=1
    ans2=max(ans2,i-l+1)
print(max(ans1,ans2))
        
