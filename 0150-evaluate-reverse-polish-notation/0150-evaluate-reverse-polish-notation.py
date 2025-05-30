class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        st = []
        for token in tokens:
            if token == "+":
                temp1 = st.pop()
                temp2 = st.pop()
                st.append(temp1+temp2)
            elif token == "-":
                temp1 = st.pop()
                temp2 = st.pop()
                st.append(temp2-temp1)
            elif token == "*":
                temp1 = st.pop()
                temp2 = st.pop()
                st.append(temp1*temp2)
            elif token == "/":
                temp1 = st.pop()
                temp2= st.pop()
                st.append(int(float(temp2) / temp1))
            else:
                st.append(int(token))
        
        return st.pop()

                