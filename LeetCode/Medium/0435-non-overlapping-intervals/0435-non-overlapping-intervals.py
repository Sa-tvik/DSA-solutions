class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        res = 0
        l = 0
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            
            if intervals[l][1] > start:
                res += 1
                if intervals[l][1] > end:
                    l = i
            else:
                l = i

        return res
            
            
