class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res = ""
        dis = []
        summ = 0
        for i in range(len(shifts)-1,-1,-1):
            summ+=shifts[i]
            dis.append(summ)
        dis.reverse()
        i = 0
        for char in s:
            res+=chr((ord(char)+dis[i]-97)%26 + 97)
            i+=1
        return res
    