class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        maxm = 0
        l = 0
        vowels= set("aeiou")

        for r in range(len(s)):
            if s[r] in vowels:
                count+=1
            
            if r-l+1>k:
                if s[l] in vowels:
                    count-=1
                l+=1
            maxm = max(maxm,count)

        return maxm

    