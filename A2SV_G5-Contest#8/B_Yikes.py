from bisect import bisect_left
n=int(input())
arr= list(map(int, input().split()))
m=int(input())
q= list(map(int, input().split()))
pri=[]
x=0
for i in arr:
    x+=i
    pri.append(x)
# print(pri)
for i in q:
    print(bisect_left(pri, i)+1)
