i = int (input())
li = list(map(int, input().split()))
cnt=0
mx = max(li)
for i in li:
    if i<mx:
        cnt += mx-i
print(cnt)
