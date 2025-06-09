class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        outDegreeCount=[0]*len(graph)
        for i in range(len(graph)):
            outDegreeCount[i]=len(graph[i])
  
        indegree=[[] for _ in range(len(graph))]
        for i in range(len(graph)):
            for j in graph[i]:
                indegree[j].append(i)
        

        q=deque([])
        result=[]
        for i in range(len(graph)):
            if outDegreeCount[i]==0:
                q.append(i)
        while q:
            node=q.popleft()
            result.append(node)
            for i in indegree[node]:
                outDegreeCount[i]-=1
                if outDegreeCount[i]==0:
                    q.append(i)
        result.sort()
        return result