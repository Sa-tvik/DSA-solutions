class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)>len(haystack):
            return -1
        if haystack == needle:
            return 0
        l = 0
        for r in range(len(needle)-1,len(haystack)):
            if haystack[l:r+1] == needle[:]:
                return l
            l+=1

        return -1