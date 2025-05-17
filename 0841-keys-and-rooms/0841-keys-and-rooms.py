class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """ 
        vis = set()
        arr = [0]

        while arr:
            curr = arr.pop(0)
            if curr in vis:
                continue
            vis.add(curr)
            for key in rooms[curr]:
                if key not in vis:
                    arr.append(key)

        return len(vis) == len(rooms)
                
        