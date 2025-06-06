class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dic = defaultdict(list)

        for i in range(len(s1)):
            dic[s1[i]].append(s2[i])
            dic[s2[i]].append(s1[i])
        
        def dfs(s, vis):
            vis.add(s)
            minm = s
            for ch in dic[s]:
                if ch not in vis:
                    temp = dfs(ch,vis)
                    minm = min(temp,minm)
            return minm

        res = []
        for s in baseStr:
            vis = set()
            res.append(dfs(s, vis))

        return "".join(res)
            