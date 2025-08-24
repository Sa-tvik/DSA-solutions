class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = [0,0]
        for i in range(len(bills)):
            if bills[i] == 5:
                change[0]+=1
            elif bills[i] == 10:
                if change[0]==0:
                    return False
                else:
                    change[0]-=1
                change[1]+=1
            else:
                if change[1] == 0 and change[0] == 0:
                    return False
                else:
                    if change[0] == 0:
                        return False
                    elif change[1] == 0:
                        if change[0]>=3:
                            change[0]-=3
                            continue
                        else:
                            return False
                    change[1]-=1
                    change[0]-=1
        return True