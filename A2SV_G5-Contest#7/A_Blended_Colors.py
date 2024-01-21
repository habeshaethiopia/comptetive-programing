for _ in range(int(input())):
    n=int(input())
    r1=input()
    r2=input()
    c=set(['G','B'])
    for i in range(n):
        if (r2[i] in c and r1[i] in c )or r1[i]==r2[i]:
            pass
        else:
            print('NO')
            break
        
    else:
        print("YES")