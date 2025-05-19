from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        m = len(maze)
        n = len(maze[0])
        q = deque()
        q.append((entrance[0], entrance[1], 0)) 
        vis = set()
        entrance_tuple = tuple(entrance)

        while q:
            x, y, dist = q.popleft()

            if (x, y) in vis:
                continue
            vis.add((x, y))

            if (x == 0 or x == m - 1 or y == 0 or y == n - 1) and (x, y) != entrance_tuple:
                return dist

            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in vis and maze[nx][ny] == ".":
                    q.append((nx, ny, dist + 1))
                    
        return -1
