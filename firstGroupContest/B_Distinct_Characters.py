s=[i for i in input()]
myset=set(s)
from collections import deque
q=deque(s[0])
c=0
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        q.append(s[i])
        for x in myset:
            if x not in q:
                if i+1<len(s) and s[i+1]==s[i]:
                    s[i]=x
                    q[-1]=x
                    break
                else:
                    s[i-1]=x
                    q[-2]=x
                # print(x,q)
                    break
    if len(q)>2:
        q.popleft()

print(''.join(s))
