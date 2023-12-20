class Solution:
    def average(self, salary: List[int]) -> float:
        mn = min(salary)
        mx = max(salary)+mn
        res= sum(salary)-mx
        dev = len(salary)-2
        return(res/dev)
        
       