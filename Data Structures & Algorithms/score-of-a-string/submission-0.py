class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        idx = 0
        idx2 = 1
        while idx2 < len(s):
            sum += abs(ord(s[idx])-ord(s[idx2]))
            idx += 1
            idx2 += 1
        return sum