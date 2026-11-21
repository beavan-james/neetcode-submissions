class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index, currString):
            if len(currString) == len(digits):
                res.append(currString)
                return
            for i in digitToChar[digits[index]]:
                backtrack(index + 1, currString + i)
        backtrack(0, "")
        return res
