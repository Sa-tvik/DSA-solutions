class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1
        for i in range(n-1,-1,-1):
            if carry == 0:
                break
            if digits[i]+carry>=10:
                carry = 1
                digits[i]+=1
                digits[i]%=10
            else: 
                digits[i]+=carry
                carry = 0

        if carry == 1:
            digits = [1]+digits
            
        return digits
