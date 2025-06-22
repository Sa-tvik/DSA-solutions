class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans=[]
        for i in range(0,len(s),k):
            ans.append(s[i:i+k])
        for j in range(k-len(ans[-1])):
            ans[-1]+=fill
        return ans