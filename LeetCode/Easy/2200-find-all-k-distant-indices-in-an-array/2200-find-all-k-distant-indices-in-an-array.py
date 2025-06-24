class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        freq = []
        res = []
        for i in range(len(nums)):
            if nums[i] == key:
                freq.append(i)

        if len(freq) == 0: return []
        j = 0
        n = len(nums)
        m = len(freq)
        for i in range(n):
            while j<m and freq[j]<i-k:      
                j+=1
            if j<m and abs(i-freq[j])<=k:
                res.append(i)

        return res
