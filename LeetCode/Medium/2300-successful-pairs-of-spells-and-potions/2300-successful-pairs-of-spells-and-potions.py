class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def helper(potions,success,spells, spell):
            l,r = 0,len(potions)-1
            temp = len(potions)
            while l<=r:
                mid = (l+r)//2
                if potions[mid]*spell>=success:
                    temp = mid
                    r = mid - 1
                else:
                    l = mid+1
            return len(potions)-temp 


        pairs = [0]*len(spells)
        potions.sort()
        for i in range(len(spells)):
            pairs[i] = helper(potions,success,spells,spells[i])

        return pairs