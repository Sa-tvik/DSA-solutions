class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(isWater), len(isWater[0])
        matrix = [[-1] * n for _ in range(m)]

        que = deque()

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    que.append((i, j, 0))
                    matrix[i][j] = 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while que:
            r, c, height = que.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] == -1:
                    matrix[nr][nc] = height + 1
                    que.append((nr, nc, height + 1))

        return matrix