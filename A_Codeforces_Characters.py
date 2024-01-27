n = int(input())
s=list('codeforces')

for i in range(n):
    letter=input()
    if letter in s:
        print('YES')
    else:
        print('NO')