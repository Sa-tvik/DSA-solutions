class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        multiplier = (len(b) - 1) // len(a) + 1
        for i in range(2):
            if b in a * (multiplier+i): return multiplier+i
        return -1