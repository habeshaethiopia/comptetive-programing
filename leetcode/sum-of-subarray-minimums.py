class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        dic = defaultdict(int)
        stack = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[i]:
                p = stack.pop()
                if stack:
                    dic[arr[p]] += i if p == 0 else (p - stack[-1]) * (i - p)
                else:
                    dic[arr[p]]+= (p+1)*(i-p)
            # print(dic,arr[i])

            stack.append(i)
        dic[arr[stack[0]]] += (stack[0] + 1) * (len(arr) - stack[0])
        for i in range(1, len(stack)):
            if len(stack) - 1 == i:
                dic[arr[stack[-1]]] += (stack[i] - stack[i - 1]) * (len(arr) - stack[i])
            else:
                dic[arr[stack[i]]] += (stack[i] - stack[i - 1]) * (
                    stack[-1] - stack[i] + 1
                )
        ans = 0
        # print(dic)
        for i in dic:
            ans += dic[i] * i
        return ans % (10**9 + 7)
