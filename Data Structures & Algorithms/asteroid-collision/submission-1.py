class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            stack.append(i)
            while len(stack) >= 2 and stack[-1] < 0 and stack[-2] > 0:
                if abs(stack[-1]) == stack[-2]:
                    stack.pop()
                    stack.pop()
                elif abs(stack[-1]) > stack[-2]:
                    stack.pop(-2)
                elif abs(stack[-1]) < stack[-2]:
                    stack.pop()
        return stack


