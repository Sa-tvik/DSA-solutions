class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj = [[] for _ in range(numCourses)]
        inDegree = [0]*numCourses

        for a, b in prerequisites:
            adj[b].append(a)
            inDegree[a]+=1

        q = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        
        schedule = []
        while len(q)>0:
            temp = q.popleft()
            schedule.append(temp)
            for i in range(len(adj[temp])):
                inDegree[adj[temp][i]]-=1
                if inDegree[adj[temp][i]] == 0:
                    q.append(adj[temp][i])

        return schedule if len(schedule) == numCourses else []

        