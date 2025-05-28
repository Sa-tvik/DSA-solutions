class Solution(object):
    def calculateScore(self, instructions, values):
        """
        :type instructions: List[str]
        :type values: List[int]
        :rtype: int
        """
        score = 0
        i = 0 
        vis = [0]*len(instructions)
        while 0<=i<len(instructions):
            if vis[i] == 1:
                break
            vis[i] = 1
            if instructions[i] == "add":
                score+=values[i]
                i+=1
            else:
                i+=values[i]

        return score
            
            
