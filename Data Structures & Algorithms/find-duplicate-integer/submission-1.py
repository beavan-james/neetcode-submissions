class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mydict = defaultdict(int)
        for i in nums:
            mydict[i]+=1
            if mydict[i] > 1:
                return i
        return -1