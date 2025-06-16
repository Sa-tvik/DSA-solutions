class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod = 1
        maxm = float('-inf')

        for i in range(len(nums)):
            prod*=nums[i]
            maxm = max(prod,maxm)
            if nums[i] == 0:
                prod = 1

        prod = 1
        
        for i in range(len(nums)-1,-1,-1):
            prod*=nums[i]
            maxm = max(prod,maxm)
            if nums[i] == 0:
                prod = 1

        return maxm
            