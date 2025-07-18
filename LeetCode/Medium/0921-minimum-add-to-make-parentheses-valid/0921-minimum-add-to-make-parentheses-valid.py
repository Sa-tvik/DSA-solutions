class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        cnt = 0
        for i in range(len(s)):
            if s[i] == "(":
                st.append(s[i])
            else:
                if not st:
                    cnt+=1
                else:
                    st.pop()
                    
        return cnt + len(st)
