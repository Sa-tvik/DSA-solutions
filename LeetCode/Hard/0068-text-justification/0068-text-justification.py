from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        l = 0
        tempLen = 0

        for i, w in enumerate(words):
            if tempLen + len(w) + (i - l) <= maxWidth:
                tempLen += len(w)
            else:
                temp = ""
                count = i - l  
                if count == 1:
                    temp += words[l]
                    temp += " " * (maxWidth - len(words[l]))
                else:
                    total_spaces = maxWidth - tempLen
                    space_between = total_spaces // (count - 1)
                    extra_spaces = total_spaces % (count - 1)

                    for j in range(l, i - 1):
                        temp += words[j]
                        temp += " " * (space_between + (1 if j - l < extra_spaces else 0))
                    temp += words[i - 1]  

                res.append(temp)
                l = i
                tempLen = len(w)

        temp = " ".join(words[l:])
        temp += " " * (maxWidth - len(temp))
        res.append(temp)

        return res
