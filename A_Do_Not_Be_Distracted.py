t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    stack = []
    flag = "YES"
    for c in a:
        if len(stack) == 0:
            stack.append(c)
        else:
            if  c not in stack :
                stack.append(c)
            elif c in stack and c != stack[-1]:
                flag = "NO"
                break
    print(flag)
 