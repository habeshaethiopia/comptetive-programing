for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    if a[0]!=b[0]:
        print('NO')
    else:
        mylist=set()
        for i in range(n):
            if a[i]>b[i]:
                if -1 not in mylist:
                    print('NO')
                    break
            elif a[i]<b[i]:
                if 1 not in mylist:
                    print('NO')
                    break
            mylist.add(a[i])
        else:
            print('YES')