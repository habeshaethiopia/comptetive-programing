s=input()
cnt=[]
for i in s:
    if cnt and cnt[-1]==i:
        cnt.pop()
    else:
        cnt.append(i)

print(''.join(cnt))