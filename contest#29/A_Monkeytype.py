for _ in range(int(input())):
    s=input()
    dic={s[i]:i+1 for i in range(26)}
    word=input()
    ans=0
    for i in range(1,len(word)):
        ans+=abs(dic[word[i-1]]-dic[word[i]])
    print(ans)