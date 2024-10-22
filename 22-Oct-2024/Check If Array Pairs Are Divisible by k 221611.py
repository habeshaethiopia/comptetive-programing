# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        pair=defaultdict(list)
        for i in arr:
            a=i%k if i>=0 else i%k
            pair[a].append(i)
           
        print(pair)
        c=0
        for i in pair:
            while pair[i]:
                f=k-i if i else 0
                if f in pair and pair[f]:
                    temp=pair[i].pop()
                    print(f,i)
                    if pair[f]:
                        pair[f].pop()
                    else:
                        continue
                    c+=1
                else:
                    pair[i].pop()
                    # print(k-i)
        n=len(arr)
        return  c>=n//2
    