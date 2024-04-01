from bisect import bisect_right
s,b = map(int, input().split())
att= list(map(int, input().split()))
ans=[]

base=[]
for i in range(b):
    d,g = map(int, input().split())
    base.append([d,g])
base.sort(key=lambda x:x[0])
pri=[]
x=0
d=[]
for i in base:
    x+=i[1]
    pri.append(x)
    d.append(i[0])

# print('defence', d)
# print('gold',pri)
# print('attack',att)
for i in att:
    x=bisect_right(d,i)
    if x>0:
        ans.append(pri[x-1])
    else:
        ans.append(0)
print(*ans)



