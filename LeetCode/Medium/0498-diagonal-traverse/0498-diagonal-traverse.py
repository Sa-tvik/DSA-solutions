from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        i, j = 0, 0
        m, n = len(mat), len(mat[0])
        res = []
        
        while len(res) < m * n:
            res.append(mat[i][j])
            
            if (i + j) % 2 == 0:
                if j == n - 1:
                    i += 1
                elif i == 0:
                    j += 1
                else:
                    i -= 1
                    j += 1
            else:
                if i == m - 1:
                    j += 1
                elif j == 0:
                    i += 1
                else:
                    i += 1
                    j -= 1
        
        return res
