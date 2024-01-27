i = int(input())
cnt = 0
for x in range(i):
    pro = list(map(int, input().split()))
    if pro.count(1) >=2:
        cnt += 1
print(cnt)