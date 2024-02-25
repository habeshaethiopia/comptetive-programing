from collections import Counter
n=int(input())
score=list(map(int, input().split()))
c=0
S=sorted(list(set(score)))
cnt=dict(Counter(score))
while len(cnt)>1        :
    for i in range(0,len(S)):
        for j in range(i+1,len(S)):
            if S[i] in cnt and S[j] in cnt:
                c+=1
                cnt[S[i]]-=1
                if cnt[S[i]]==0:
                    del cnt[S[i]]
                break
print (c)