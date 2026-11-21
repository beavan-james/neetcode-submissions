class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mymax = 0
        l,r = 0, len(heights) - 1
        while l < r:
            score = (r-l) * (min(heights[r],heights[l]))
            mymax = max(mymax, score)
            if heights[r] > heights[l]:
                l += 1
            else:
                r-=1
        return mymax