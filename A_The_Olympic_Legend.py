n = int(input())

for i in range(n):
    lst = list(map(int, input().split()))
    c=0
    for i in lst[1:]:
        if lst[0]  < i:
            c+=1
    print (c)