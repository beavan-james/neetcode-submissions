class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        mylist = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    lis = [nums[i], nums[l], nums[r]]
                    lis.sort()
                    if lis in mylist:
                        lis = []
                    else:
                        mylist.append(lis)
                    l+=1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r-=1
                else:
                    l+=1
        
        return mylist