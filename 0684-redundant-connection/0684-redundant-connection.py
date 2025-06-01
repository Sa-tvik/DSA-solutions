class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent, rank = [], []
        for i in range(len(edges)+1):
            parent.append(i)
            rank.append(1)

        def find(n):
            p = parent[n]
            while p!=parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        for x,y in edges:
            parX, parY = find(x), find(y)
            if parX!=parY:
                if rank[parX]>=rank[parY]:
                    parent[parY] = parX
                    rank[parX]+=1
                else:
                    parent[parX] = parY
                    rank[parY]+=1
            else:
                return [x,y]


