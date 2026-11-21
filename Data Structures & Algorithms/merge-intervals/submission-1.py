class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []
        l = 0
        for r in range(len(intervals)):
            if intervals[l][0] <= intervals[r][0] <= intervals[l][1]:
                intervals[l][1] = max(intervals[l][1], intervals[r][1])
            else:
                res.append(intervals[l])
                l = r
        
        res.append(intervals[l])
        return res