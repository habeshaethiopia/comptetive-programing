t  = int(input())
for i in range(t):
    n = int(input())
    s = input()
    for i in range(int(n/2)):
        if (s[0] == '0' and s[-1] == '1')or(s[0] == '1' and s[-1] == '0'):
            s = s[1:-1]
        else:
            break
        
    print(len(s))
    