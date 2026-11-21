class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        mymap = defaultdict(int)
        for i in s1:
            mymap[i] += 1
        l, r = 0, len(s1)
        while r <= len(s2):
            mymap2 = defaultdict(int)
            string = s2[l:r]
            for i in string:
                mymap2[i] += 1
            if mymap2 == mymap:
                return True
            l+=1
            r+=1
        return False

