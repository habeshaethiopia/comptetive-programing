for _ in range(int(input())):
    n = int(input())
    s = [i for i in input()]
    flag = []
    l = 0
    r = len(s)-1
    for l in range(n // 2):
        if s[l] == s[r]:
            pass
        else:
            s[l] = s[r]
            flag.append(l)
        r-=1
    
    if not flag or flag == list(range(flag[0],flag[-1]+1)):
            print('Yes') 
    else:
            print('No')
