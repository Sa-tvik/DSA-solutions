class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = {}
        for t in tasks:
            count[t] = count.get(t, 0) + 1
        f_max = max(count.values())
        max_count = sum(1 for v in count.values() if v == f_max)
        return max(len(tasks), (f_max - 1) * (n + 1) + max_count)