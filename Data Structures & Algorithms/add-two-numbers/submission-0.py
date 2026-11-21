# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ""
        str2 = ""
        while (l1 != None):
            str1 += str(l1.val)
            l1 = l1.next
        while (l2 != None):
            str2 += str(l2.val)
            l2 = l2.next
        str1 = str1[::-1]
        str2 = str2[::-1]
        res = int(str1) + int(str2)
        res = str(res)
        res = res[::-1]
        dummy = ListNode()
        curr = dummy
        for char in res:
            curr.next = ListNode(int(char))
            curr = curr.next
            
        return dummy.next