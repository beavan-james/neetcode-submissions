class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        for i in digits:
            string += str(i)
        num = int(string)
        num +=1
        mylist = []
        for i in str(num):
            mylist.append(int(i))
        return mylist