n=int(input())
m=int(input())
a=[]
for i in range(n):
    a1=int(input())
    a.append(a1)
a.sort(reverse=True)
x=0
c=0
for i in a:
    x+=i
    c+=1
    if x>=m:
        print (c)
        break

