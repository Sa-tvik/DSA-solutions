class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = [""]*26
        mapped = {}
        words = s.split()

        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):
            idx = ord(pattern[i]) - ord('a')
            word = words[i]

            if dic[idx] != "":
                if dic[idx] != word:
                    return False
            else:
                if word in mapped:
                    return False 
                dic[idx] = word
                mapped[word] = pattern[i]

        return True
