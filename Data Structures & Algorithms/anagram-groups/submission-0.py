class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #brute force
        mapmap = defaultdict(list)
        for i in strs:
            sort = "".join(sorted(i))
            mapmap[sort].append(i)
        mylist = []
        for i in mapmap.values():
            mylist.append(i)
        return mylist