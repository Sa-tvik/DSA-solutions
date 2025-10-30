class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m,n = len(str1), len(str2)
        i = 0
        tempRes = ""
        res = ""
        if str1 + str2 != str2 + str1:
            return tempRes

        while i < m and i<n:
            if str1[i] != str2[i]:
                return tempRes
            tempRes+=str1[i]
            i+=1
            if m>=n:
                if str1 == tempRes*(m//len(tempRes)) and str2 == tempRes*(n//len(tempRes)):
                    res = tempRes
                elif str2 == tempRes*(n//len(tempRes)) and str1 == tempRes*(m//len(tempRes)):
                    res = tempRes

        return res 
                  
