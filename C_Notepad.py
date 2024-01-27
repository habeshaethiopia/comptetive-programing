n = int(input())

for i in range(n):
    n=int(input())
    s=input()
    srt=0
    # lis = 
    for i in range(1,n):
        if s.count(s[srt:i]) > 1:
            if len(s[srt:i])>1:
                print('YES')
                break
        else:
            srt+=1
    else:
        print('NO')