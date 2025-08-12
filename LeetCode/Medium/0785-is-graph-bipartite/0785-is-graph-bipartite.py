class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        q = deque()
        vis = defaultdict(list)
        for start in range(len(graph)):
            if start in vis:
                continue
            q.append((start, 0))
            while len(q)>0:
                x,y = q.popleft()
                if x in vis and y not in vis[x]: 
                    return False
                elif x in vis and y in vis[x]:
                    continue
                vis[x].append(y)
                for i in range(len(graph[x])):
                    q.append([graph[x][i],y^1])
        return True