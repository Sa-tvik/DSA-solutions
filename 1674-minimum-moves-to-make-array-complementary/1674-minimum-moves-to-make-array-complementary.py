class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        n = len(nums)
        diffr = [0]*(2*limit + 2)
        for i in range(n//2):
            a,b = nums[i],nums[n-1-i]
            comp = nums[i] + nums[n-1-i]
            low  = 1 + min(a,b)
            high = limit + max(a,b)
            
            diffr[2] +=2
            diffr[low] -=1
            diffr[comp] -=1
            diffr[comp+1]+=1
            diffr[high+1]+=1
         
        moves = 0
        minMoves = float('inf')
        for i in range(2, 2*limit+2):
            moves+=diffr[i]
            minMoves = min(minMoves,moves)
            
        return minMoves
                
                
                    
                
         
        
            