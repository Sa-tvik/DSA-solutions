class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adjacency_list = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adjacency_list[b].append(a)

        visit_status = [0] * numCourses

        def dfs(course):
            if visit_status[course] == 1:
                return False
            if visit_status[course] == 2:
                return True

            visit_status[course] = 1
            for neighbor in adjacency_list[course]:
                if not dfs(neighbor):
                    return False

            visit_status[course] = 2
            return True

        for c in range(numCourses):
            if visit_status[c] == 0:
                if not dfs(c):
                    return False
        return True