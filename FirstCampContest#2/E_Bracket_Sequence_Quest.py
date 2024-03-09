s=input()
l=0
sub=0
stack=[]
mx=0
for i in s:
    if i=='(':
        stack.append('(')
    elif stack and i==')':
        stack.pop()
        l+=2
    elif i==")":
        if l:
            sub+=1
        l=0
    mx=max(l,mx)
    # print(stack)
if l:
    sub+=1
if mx and sub:
    print(mx,sub)
else:
    print(0,1)