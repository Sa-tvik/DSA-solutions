class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:       
        n = len(nums1)
        m = len(nums2)
        dp = [0]*(m+1)
        maxm = 0
         
        for ind1 in range(1,n+1):
            temp = [0]*(m+1)
            for ind2 in range(1,m+1):
                if nums1[ind1-1] == nums2[ind2-1]:
                    temp[ind2] = 1 + dp[ind2-1]
                else:
                    temp[ind2] = 0
                maxm = max(maxm, temp[ind2])
            dp = temp
            
        return maxm