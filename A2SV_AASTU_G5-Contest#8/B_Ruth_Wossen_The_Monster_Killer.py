n=int(input())
cost=list(map(int, input().split()))
srt=sorted(cost)
pri=[0]
pris=[0]
x=0
y=0
for idx,i in enumerate(cost):
    x+=i
    y+=srt[idx]
    pri.append(x)
    pris.append(y)

for i in range(int(input())):
    q=list(map(int, input().split()))
    if q[0]==1:
        print(pri[q[2]]-pri[q[1]-1])
    else:
        print(pris[q[2]]-pris[q[1]-1])
    
