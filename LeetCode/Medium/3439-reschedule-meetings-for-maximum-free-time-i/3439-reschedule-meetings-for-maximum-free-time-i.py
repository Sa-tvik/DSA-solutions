class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        nums = [startTime[0]]  
        for i in range(1, len(startTime)):
            nums.append(startTime[i] - endTime[i - 1]) 
        nums.append(eventTime - endTime[-1]) 

        window_sum = 0
        max_free_time = 0
        for i in range(len(nums)):
            window_sum += nums[i]
            if i >= k:
                max_free_time = max(max_free_time, window_sum)
                window_sum -= nums[i - k] 

        return max_free_time