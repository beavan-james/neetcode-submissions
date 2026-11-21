class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapmap = defaultdict(int)
        for i in nums:
            mapmap[i] += 1
            if mapmap[i] > (len(nums)/2):
                return i
        return -1