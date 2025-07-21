class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ""
        temp = [0,""]
        for i in range(len(s)):
            if s[i] == temp[1]:
                temp[0]+=1
            else:
                temp[0] = 1
                temp[1] = s[i]
            if temp[0]>=3:
                continue
            else:
                res+=temp[1]

        return res
        