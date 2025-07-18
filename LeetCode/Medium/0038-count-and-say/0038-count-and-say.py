class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        temp = self.countAndSay(n-1)
        res = []
        i = 1
        cnt = 1
        while i < len(temp):
            if temp[i] == temp[i - 1]:
                cnt += 1
            else:
                res.append(str(cnt))
                res.append(temp[i - 1])
                cnt = 1  
            i += 1
        res.append(str(cnt))
        res.append(temp[-1])


        return "".join(res)
            

