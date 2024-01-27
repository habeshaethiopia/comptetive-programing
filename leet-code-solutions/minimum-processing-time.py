class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)
        n=len(tasks)//len(processorTime)
        Sum=[]
        for i in range(len(processorTime)):
            s= max(tasks[i*n : n*(i+1)])+processorTime[i]
            print(tasks[i*n : n*(i+1)],processorTime[i])
            Sum.append(s)
        print(Sum)
        return max(Sum)
