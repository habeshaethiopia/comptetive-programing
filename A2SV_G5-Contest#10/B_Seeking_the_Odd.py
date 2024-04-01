for _ in range(int(input())):
    n=int(input())
    x=2
    flag=False
    while x<= n:
        if n%x==0:
            x*=2
        else:
            flag=True
            break
    print('YES' if  flag else 'NO')