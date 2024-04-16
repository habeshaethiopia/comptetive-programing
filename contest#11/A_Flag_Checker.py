n,m=map(int,input().split())
mtx=[]
pri=set()
for i in range(n):
    row=[i for i in input()]
    my=set(row)

    if len(my)==1 and pri!=my:
        mtx.append(row)
        pri=my
    else:
        print('NO')
        break
else:
    print("YES")