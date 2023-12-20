def count(s,pattern):
    count=0
    for i in range(len(s)):
        if s[i:i+len(pattern)]==pattern:
            count+=1
    return count
n = int(input())

for i in range(n):
    size=int(input())
    s=input()
    if count(s,"abacaba")> 1:
        print('No')
        continue
    else:
        s=list(s)
        pattern = list("abacaba")
        for i in range(size-6):
            temp=s[i:i+7]
            for j in range(7):
                if temp[j]=='?':
                    temp[j]=pattern[j]
            if temp==pattern:
                news=s[:i]+temp+s[i+7:]
                news=''.join(news)
                if count(news,"abacaba")==1:
                    print('Yes')
                    print(news.replace('?','d'))
                    break

        else:
            print('No')
                    