class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ""

        count = defaultdict(int)
        for ch in t:
            count[ch] += 1

        required = len(count)
        formed = 0
        window = defaultdict(int)

        l = 0
        minm = [float('inf'), 0, 0]

        for r, ch in enumerate(s):
            if ch in count:
                window[ch] += 1
                if window[ch] == count[ch]:
                    formed += 1

            while formed == required:
                if (r - l + 1) < minm[0]:
                    minm = [r - l + 1, l, r]

                if s[l] in count:
                    window[s[l]] -= 1
                    if window[s[l]] < count[s[l]]:
                        formed -= 1
                l += 1

        return "" if minm[0] == float('inf') else s[minm[1]:minm[2]+1]