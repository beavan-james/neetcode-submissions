class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mapmap = {}
        for i in range(len(position)):
            mapmap[position[i]] = (target - position[i]) / speed[i]
        position.sort(reverse=True)
        print(position)
        stack = []
        for i in position: 
            stack.append(mapmap[i])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
            