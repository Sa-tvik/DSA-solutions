class Solution(object):
    def leastInterval(self, tasks, n):
        
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        
        freq = {}
        available = []
        cooldown = []

        # frequency setup
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        # available setup
        for task in freq:
            heapq.heappush(available, (-freq[task], task))

        intervals = 0
        while available or cooldown:
            if not available and cooldown:
                intervals = cooldown[0][0]
            else:
                intervals += 1

            while cooldown and cooldown[0][0] <= intervals:
                _, freq, task = heapq.heappop(cooldown)
                heapq.heappush(available, (freq, task))

            if available:
                frequency, task = heapq.heappop(available)
                if frequency < -1:
                    heapq.heappush(cooldown, (intervals + n + 1, frequency + 1, task))
        return intervals