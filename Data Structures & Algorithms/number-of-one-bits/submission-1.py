class Solution:
    def hammingWeight(self, n: int) -> int:
        str_int = bin(n)
        sum = 0

        for char in str_int:
            if char == "1":
                sum += 1
        
        return sum