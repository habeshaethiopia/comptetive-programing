t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    sm=0
    pri=[0]
    for i in a:
        sm+=i
        pri.append(sm)
    for p in range(q):
        l, r, k = map(int, input().split())
        sm=pri[-1]-(pri[r]-pri[l-1]) +(r-l+1)*k
        print ('YES') if sm%2 else print ("NO")