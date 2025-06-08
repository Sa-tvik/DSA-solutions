class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        st = []
        res = []

        suffix_min = [''] * n
        suffix_min[-1] = s[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(s[i], suffix_min[i + 1])

        for i in range(n):
            st.append(s[i])
            while st and (i == n - 1 or st[-1] <= suffix_min[i + 1]):
                res.append(st.pop())

        return ''.join(res)