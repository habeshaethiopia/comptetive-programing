from collections import Counter
for _ in range(int(input())):
    n=int(input())
    arr= list(map(int, input().split()))
    x=0
    for i in range(n):
        x+=arr[i]-i
        if x<0:
            print('NO')
            break
    else:
        print('YES')
        
    