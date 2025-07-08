class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = 0
        if dividend*divisor<0: 
            neg = 1 
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            result += multiple

        result = result if not neg else -result
        return min(max(-2**31, result), 2**31 - 1)