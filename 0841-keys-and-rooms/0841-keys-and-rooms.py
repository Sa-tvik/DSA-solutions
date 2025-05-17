class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """ 
        vis = []
        arr = []
        idx = 1
        vis.append(0)
        arr.append(0)
        for i in range(len(rooms[0])): 
            arr.append(rooms[0][i])

        while idx < len(arr):
            if arr[idx] not in vis: 
                vis.append(arr[idx])
            else: 
                continue

            if len(vis) == len(rooms): return True

            for i in range(len(rooms[arr[idx]])):
                if rooms[arr[idx]][i] not in arr:
                    arr.append(rooms[arr[idx]][i])
            idx+=1
        return False
                
        