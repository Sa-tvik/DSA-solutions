class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = []
        for i in range(len(nums)):
            temp = nums[i]
            digSum= 0
            while temp>0:
                digSum += temp%10
                temp //= 10
            res.append([digSum,nums[i],i])
        res.sort(key=lambda x: (x[0],x[1]))
        cnt = 0
        i = 0
        while i<len(nums):
            if res[i][2] != i:
                swap_idx = res[i][2]
                res[i], res[swap_idx] = res[swap_idx], res[i]
                cnt+=1
            else:
                i+=1

        return cnt
        

        
    
                
            
        
        