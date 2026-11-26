class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        myset = set()
        def backtrack(i):
            if i >= len(nums):
                mine = curr.copy()
                mine.sort()
                if tuple(mine) not in myset:
                    myset.add(tuple(mine))
                    res.append(mine)
                return
            curr.append(nums[i])
            backtrack(i + 1)
            curr.pop()
            backtrack(i + 1)

        backtrack(0)
        return res