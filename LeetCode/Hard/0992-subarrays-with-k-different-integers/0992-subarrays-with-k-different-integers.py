class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(nums,k):
            window = defaultdict(int)
            res = 0
            l = 0
            for i in range(len(nums)):
                window[nums[i]]+=1
                while len(window)>k:
                    window[nums[l]]-=1
                    if window[nums[l]] == 0:
                        window.pop(nums[l])
                    l+=1
                res += i-l+1
            return res
        return atMostK(nums, k) - atMostK(nums,k-1)

                
                