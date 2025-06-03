class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        for s in s1:
            freq[s] = freq.get(s, 0) + 1

        l = 0
        cnt = 0
        required = len(freq)
        window_size = len(s1)

        for r in range(len(s2)):
            if s2[r] in freq:
                freq[s2[r]] -= 1
                if freq[s2[r]] == 0:
                    cnt += 1

            if r - l + 1 > window_size:
                if s2[l] in freq:
                    if freq[s2[l]] == 0:
                        cnt -= 1
                    freq[s2[l]] += 1
                l += 1

            if cnt == required and r - l + 1 == window_size:
                return True

        return False
