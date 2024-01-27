n, q = map(int, input().split())
a = list(map(int, input().split()))
p=[0]*(n+1)
for i in range(q):
    l,r=map(int,input().split())
    p[l-1]+=1
    p[r]-=1
a.sort()
pri=[]
sm=0
for i in p[:-1]:
    sm+=i
    pri.append(sm)
sm=0
pri.sort()
for i in range(n):
    sm+=a[i]*pri[i]
print(sm)
# print(a,pri)
