from math import lcm
n=int(input())
arr= list(map(int, input().split()))
x=1

for i in range(n):
    
    while arr[i]%2==0:
        arr[i]//=2
    while arr[i]%3==0:
        arr[i]//=3
    if i>0:
        if arr[i]!= arr[i-1]:
            print('No')
            break
else:
    print('Yes')
