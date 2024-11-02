for _ in range(int(input())):
    a,b,c,n = map(int, input().split())

    sm=sum([a,b,c,n])
    if sm %3==0:
        if sm//3>= max([a,b,c]):
            print("YES")
        else:
            print("NO")   
    else:
        print("NO")   
    