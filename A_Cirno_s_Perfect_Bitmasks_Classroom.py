for _ in range(int(input())):
    z=int(input())
    # print(z,'=>' ,end=' ')
    x=bin(z)[2:]
    ans=['0']*(len(x))
    n=len(x)
    flag=True
    for i in range(n-1,-1,-1):
        if x[i]=='1':
            ans[i]='1'
            y=int(''.join(ans),2)
            if y& z >0 and y^z >0:
                print(y)
                break
            else:
                for j in range(n-1,-1,-1):
                    if x[j]=='0':
                        ans[j]='1'
                        y=int(''.join(ans),2)
                        if y& z >0 and y^z >0:
                            print(y)
                            flag=False
                            
                            break
    else:
        if flag:
            y=int('1'+''.join(ans),2)
            
            print(y)