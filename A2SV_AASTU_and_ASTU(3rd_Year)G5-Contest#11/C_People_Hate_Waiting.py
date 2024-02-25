n = int(input())
nums = list(map(int, input().split()))
ans = []
x = 0
for i in nums:
    ans.append(x)
    x += i
x = 0
for i in range(n):
    if ans[i] <= nums[i]:
        x += 1
print(x)
