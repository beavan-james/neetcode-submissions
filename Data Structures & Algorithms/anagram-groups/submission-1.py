class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapmap = defaultdict(list)
        for i in strs:
            mystring = "".join(sorted(i))
            mapmap[mystring].append(i)
        res = []
        for i in mapmap.values():
            res.append(i)
        return res