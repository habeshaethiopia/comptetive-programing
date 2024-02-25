stack=[]
ans=0
c=1
for _ in range(2*int(input())):
    command = input().split()
    n=int(command[1]) if len(command)>1 else 0
    if command[0] == 'add':
        # temp=False
        # x2=[]
        # while stack and stack[-1]<n:
        #     temp=True
        #     x2.append(stack.pop())
        # if temp:
        #     ans+=1
        stack.append(n)
        # stack+=x2
    else:
        if stack[-1]!= c:
            stack.sort(reverse=True)
            ans+=1
        if stack:
            stack.pop()
        c+=1
        
print(ans)
