for _ in range(int (input())):
    n,  h=map(int, input().split())
    x=0
    for i in range(n):
        w,l=map(int, input().split())
        x+=max(w,l)
    if x>=h:
        print('YES')
    else:
        print('NO')
