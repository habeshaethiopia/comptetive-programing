na=int(input())
aastu=list(map(int, input().split()))
ni=int(input())
aait=list(map(int, input().split()))
aastu.sort()
aait.sort()
c=0
for i in range(na):
    for j in range(len(aait)):
        if abs(aastu[i]-aait[j])<=1:
            aait.remove(aait[j])
            c+=1
            break
print(c)
