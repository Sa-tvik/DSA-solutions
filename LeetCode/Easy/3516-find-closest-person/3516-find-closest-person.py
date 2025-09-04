class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        xz = abs(x-z)
        yz = abs(y-z)

        if xz == yz:
            return 0
        elif xz>yz:
            return 2
        else: return 1