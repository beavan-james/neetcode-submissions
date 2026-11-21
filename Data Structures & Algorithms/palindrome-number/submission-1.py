class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        mystr = str(x)
        if mystr == mystr[::-1]:
            return True
        else:
            return False