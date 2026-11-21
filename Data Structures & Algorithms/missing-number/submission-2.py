class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mapmap = defaultdict(int)
        for i in nums:
            mapmap[i] += 1
        for x in mapmap.keys():
            if x == 0:
                if mapmap[0] == 0:
                    return 0
                else:
                    pass
            elif mapmap[x-1] == 0:
                return x-1
        return len(nums)