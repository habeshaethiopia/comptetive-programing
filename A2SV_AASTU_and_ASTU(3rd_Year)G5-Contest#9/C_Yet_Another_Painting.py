t = int(input())
for _ in range(t):
    n=int(input())
    r = list(map(int, input().split()))
    m=int(input())
    b = list(map(int, input().split()))
    pri=[0]
    x=0
    for i in range(max(n,m)):
        if r[0]>b[0]:
            if i<n:
                x+= r[i]
                pri.append(x)
            if i<m:
                x+=b[i]
                pri.append(x)
        else:
            if i<m:
                x+=b[i]
                pri.append(x)
            if i<n:
                x+= r[i]
                pri.append(x)
    print(max(pri))