class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        mapmap = defaultdict(int)
        for i in nums:
            mapmap[i] += 1
            if mapmap[i] > (len(nums)/3):
                res.append(i)
        myset = set(res)
        return list(myset)