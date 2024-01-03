class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        
        tasks.sort(reverse= True)
        processorTime.sort()
        j = 0
        arr = []
        for i in range(0,len(tasks),4):
            arr.append(processorTime[j] + tasks[i])
            j += 1
        
        return max(arr)
