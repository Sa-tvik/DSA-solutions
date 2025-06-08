class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        shots = 0
        i = 0
        while i < len(points):
            temp = points[i][1]
            while i<len(points)-1 and points[i+1][0] <= temp <= points[i+1][1]:
                i+=1
            i+=1
            shots+=1
        return shots