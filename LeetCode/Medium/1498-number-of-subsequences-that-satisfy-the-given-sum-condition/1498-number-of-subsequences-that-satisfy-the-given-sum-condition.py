class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        res = 0
        nums.sort()
        r = len(nums)-1
        mod = 10**9 + 7
        l = 0
        while l<=r:
            if nums[l] + nums[r]> target:
                r-=1
            else:
                res+= (2**(r-l))
                res%=mod
                l+=1
        return res%mod

            