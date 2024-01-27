n = int(input())
com="codeforces"
for i in range(n):
    s = input()
    cnt=0
    for i in range(len(com)):
        if s[i]!=com[i]:
            cnt +=1
    print (cnt)