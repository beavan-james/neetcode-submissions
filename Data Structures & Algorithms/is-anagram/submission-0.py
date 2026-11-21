class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = Counter(s)
        list2 = Counter(t)
        if list1 == list2:
            return True
        return False