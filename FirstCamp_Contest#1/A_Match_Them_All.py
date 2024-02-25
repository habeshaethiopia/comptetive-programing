
for _ in range(int(input())):
    n=int(input())
    cnt={}
    for i in range(n):
        s=input()
        for i in s:
            cnt[i]=cnt.get(i,0)+1
    for i in cnt:
        if cnt[i]%n:
            print('NO')
            break
    else:
        print('YES')
