class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        seen = set()
        candidates.sort()
        def backtrack(lower, mysum):
            #if mysum == target:
            #    if tuple(temp) in seen:
            #        return
            #    seen.add(tuple(temp))
            #    res.append(temp.copy())


            if mysum == target:
                res.append(temp.copy())
                return

            for i in range(lower, len(candidates)):
                if i > lower and candidates[i] == candidates[i-1]:
                    continue

                if mysum + candidates[i] > target:
                    break

                temp.append(candidates[i])
                backtrack(i + 1, mysum + candidates[i])
                temp.pop()
        backtrack(0, 0)
        return res
