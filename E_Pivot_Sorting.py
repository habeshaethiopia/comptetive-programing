n = int(input())
import math
for i in range(n):
    size = int(input())
    lst = list(map(int, input().split()))
    x = 0
    for i in range(size-1):
        if lst[i]>lst[i+1]:
            x= max(x, math.ceil((lst[i]+lst[i+1])/2))
    sort =[abs(i-x) for i in lst]
    for i in range(size-1):
        if sort[i] > sort[i+1]:
            print(-1)
            break
    else:
        print(x)