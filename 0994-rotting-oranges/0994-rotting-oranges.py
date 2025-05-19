class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque

        m = len(grid)
        n = len(grid[0])
        vis = []
        q = deque()
        maxTime = 0
        fCount = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fCount+=1
                if grid[i][j] == 2:
                    q.append([i, j, 0]) 
        
        while q:
            temp = q.popleft()
            x, y, t = temp
            vis.append([x,y])

            if x+1 < m and grid[x+1][y] == 1:
                grid[x+1][y] = 2
                q.append([x+1, y, t+1])
                maxTime = max(maxTime,t+1)
                fCount-=1
        
            if x-1 >= 0 and grid[x-1][y] == 1:
                grid[x-1][y] = 2
                q.append([x-1, y, t+1])
                maxTime = max(maxTime,t+1)
                fCount-=1
        
            if y+1 < n and grid[x][y+1] == 1:
                grid[x][y+1] = 2
                q.append([x, y+1, t+1])
                maxTime = max(maxTime,t+1)
                fCount-=1
            if y-1 >= 0 and grid[x][y-1] == 1:
                grid[x][y-1] = 2
                q.append([x, y-1, t+1])
                fCount-=1
                maxTime = max(maxTime,t+1)
        
        if fCount >0: return -1
        
        return maxTime
            
        
        
            

        