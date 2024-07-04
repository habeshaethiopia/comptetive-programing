# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1=-prices[0]
        buy2=-prices[0]

        prof1=0
        prof2=0
        for i in prices:
            buy1=max(buy1, -i)
            prof1=max(prof1,buy1+i)
            buy2=max(buy2, prof1-i)
            prof2=max(prof2, i+buy2)
        return prof2