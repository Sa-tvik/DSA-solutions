class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        n = len(temperatures)
        answer = [0]*n

        for i in range(n-1,-1,-1):
            while len(stack)>0 and temperatures[i]>=temperatures[stack[-1]]:
                stack.pop()

            if stack:
                answer[i] = stack[-1]-i
            stack.append(i)

        return answer

            
        