class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        
        def dfs(r, c, visited, original):
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original  or (r, c) in visited:
                return

            image[r][c] = color

            visited.add((r, c))
            dfs(r + 1, c, visited, original) 
            dfs(r - 1, c, visited, original) 
            dfs(r, c + 1, visited, original) 
            dfs(r, c - 1, visited, original)

            return
        
        
        dfs(sr, sc, set(),image[sr][sc])
            
        return image