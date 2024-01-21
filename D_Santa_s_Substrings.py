s=[]
mx=0
mxs=""
n=int(input())
for _ in range(n):
    temp=input().strip()
    if len(temp)>mx:
        mx=len(temp)
        mxs=temp[:]
   
    s.append(temp)
for i in range(n):
    for j in range(i,n):
        if s[j] in s[i]:
            s[j] ,s[i]= s[i], s[j]
tr=False

for i in range(n-1):
    for j in range(i, n):
        if s[i] not in s[j]:
            print("NO")
            tr=True
            break
    if tr:
        break
if not tr:
    print('YES')
    print(*s, sep='\n')