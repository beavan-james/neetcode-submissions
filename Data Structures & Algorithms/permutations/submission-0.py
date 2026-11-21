class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        res = []
        mylist = []
        visit = [False] * len(nums)
        def perm():
            if len(mylist) == length:
                res.append(mylist.copy())
                return
            for i in range(length):
                if visit[i] == False:
                    mylist.append(nums[i])
                    visit[i] = True
                    perm()
                    mylist.pop()
                    visit[i] = False
        perm()
        return res
