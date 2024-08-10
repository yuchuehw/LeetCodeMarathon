class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = set(rooms[0])
        seen = {0}
        while keys-seen:
            if len(seen) == len(rooms):
                return True
            for k in keys-seen:
                seen.add(k)
                keys.update(rooms[k])
        return len(seen) == len(rooms)
