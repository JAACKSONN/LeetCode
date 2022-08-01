# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        dummy = res
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            cur = val1 + val2 + carry
            carry = cur // 10
            res.next = ListNode(cur % 10)
            
            res = res.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        if carry:
            res.next = ListNode(carry)
        return dummy.next