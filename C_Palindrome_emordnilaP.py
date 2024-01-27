n = int(input())
for i in range(n):
    size = int(input())
    s= input().split()
    for i in range(size):
        if s[i] in s[i+2:]:
            print('YES')
            break
    else:
        print('NO')
    