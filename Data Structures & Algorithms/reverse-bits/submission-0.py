class Solution:
    def reverseBits(self, n: int) -> int:
        res = bin(n)
        res = res.split("b")
        res = res[1]
        add = "0" * (32 - len(res))
        res = add + res
        res = res[::-1]
        res = int(res, 2)
        return res