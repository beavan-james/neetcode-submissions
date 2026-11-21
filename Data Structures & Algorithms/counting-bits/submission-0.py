class Solution:
    def countBits(self, n: int) -> List[int]:
        mystack = []
        for i in range(n + 1):
            count = 0
            for x in bin(i):
                if x == "1":
                    count += 1
            mystack.append(count)
        return mystack