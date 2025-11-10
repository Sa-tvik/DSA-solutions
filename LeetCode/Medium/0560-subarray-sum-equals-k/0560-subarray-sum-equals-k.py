class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        pSum = 0
        res = 0
        for i in range(len(nums)):
            pSum += nums[i]
            if pSum-k in dic:
                res += dic[pSum-k]
            dic[pSum]+=1
        return res