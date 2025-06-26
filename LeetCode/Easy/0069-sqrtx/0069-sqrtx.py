class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            temp = mid*mid
            if temp == x:
                return mid
            elif temp < x:
                left = mid + 1
            else:
                right = mid - 1
        return right