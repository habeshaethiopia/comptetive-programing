n = int(input())

for i in range(n):
    size = input()
    
    lst = list(map(int, input().split()))
    size = len(lst)
    count={}
    c=0
    for i in range(size):
        if lst[i]-i in count:
            count[lst[i]-i] += 1
            c += count[lst[i]-i]
        else:
            count[lst[i]-i] = 0
    print(c)