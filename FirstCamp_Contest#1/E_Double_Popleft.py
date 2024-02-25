from collections import deque
n,q=map(int, input().split())
my=deque(list(map(int, input().split())))
AB=[]
mx=max(my)
for i in range(q):
    m=int(input())
    if m<len(AB):
        continue
    for x in range(len(AB),20):
        a=my.popleft()
        b=my.popleft()
        if a=mx():co
        AB.append([a,b])
        if a>b:
            my.insert(0,a)
            my.append(b)
        else:
            my.insert(0,b)
            my.append(a)
    print(AB)
    print(*AB[m-1])
