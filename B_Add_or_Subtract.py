n = int(input())
for i in range(n):
    s=list(map(int,input().split()))
    if s[0]+s[1]==s[2]:
        print('+')
    else:
        print('-')