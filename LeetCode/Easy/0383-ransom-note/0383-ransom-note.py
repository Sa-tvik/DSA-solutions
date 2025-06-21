class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = {}

        for c in magazine:
            freq[c] = 1 + freq.get(c, 0)

        for c in ransomNote:
            if c not in freq or freq[c] <= 0:
                return False
            freq[c] -= 1
        
        return True