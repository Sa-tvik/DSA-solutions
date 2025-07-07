class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap = []  
        i = 0
        n = len(events)
        count = 0
        lastDay = max(end for _, end in events)
        for day in range(1,lastDay+1):
            while i<n and day==events[i][0]:
                    heapq.heappush(heap,events[i][1])
                    i+=1

            while heap and heap[0]<day:
                heapq.heappop(heap)

            if heap:
                heapq.heappop(heap)
                count += 1  

            if i == n and not heap:
                break

        return count


