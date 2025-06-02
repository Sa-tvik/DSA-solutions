class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        def dfs(current, distance, edges, distances):
            if current == -1:
                return
            
            if distances[current] == -1:
                distances[current] = distance
                distance += 1
                current = edges[current]
                dfs(current,distance,edges,distances)
    
        dist1 = []
        dist2 = []
        for i in range(len(edges)):
            dist1.append(-1)
            dist2.append(-1)

        dfs(node1,0,edges,dist1)
        dfs(node2,0,edges,dist2)

        result = -1
        min_dist = float('inf')

        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_dist:
                    min_dist = max_dist
                    result = i

        return result