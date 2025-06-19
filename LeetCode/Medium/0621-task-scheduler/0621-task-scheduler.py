class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        available = []
        interval = 0
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        for task in freq:
            heapq.heappush(available, -freq[task])

        while available:
            cooldown = []
            cycle = n+1
            while cycle and available:
                maxm = -heapq.heappop(available)
                if maxm>1:
                    cooldown.append(maxm-1)
                cycle-=1
                interval+=1
            
            for task in cooldown:
                heapq.heappush(available,-task)

            if not available:
                return interval
            interval+=cycle

        return interval
            




        
