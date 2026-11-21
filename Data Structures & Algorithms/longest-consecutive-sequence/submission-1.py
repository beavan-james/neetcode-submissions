class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        mymax = 1
        for i in num_set:
            if i - 1 not in num_set: #min
                curr = i
                count = 1
                while curr + 1 in num_set:
                    curr += 1
                    count += 1
                if count > mymax:
                    mymax = count
        return mymax