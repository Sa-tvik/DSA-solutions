class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or board[r][c] == 'X' or (r, c) in visited:
                return
            visited.add((r, c))   

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == "O" and (nr, nc) not in visited:         
                    dfs(nr, nc)

        m = len(board)
        n = len(board[0])     
        visited = set()

        for r in range(m):
            for c in [0, n - 1]:
                if board[r][c] == 'O' and (r, c) not in visited:
                    dfs(r, c)

        for c in range(n):
            for r in [0, m - 1]:
                if board[r][c] == 'O' and (r, c) not in visited:
                    dfs(r, c)

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O' and (r, c) not in visited:
                    board[r][c] = 'X'
