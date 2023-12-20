n = int(input())

for i in range(n):
    s = input()
    old=""
    for i in range(len(s)):
        if i%2==0:
            old += s[i]
    old+=s[-1]
    print (old)