# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Then numbers are in reverse order so we can traverse left to right using head and maintain carry if needed. Problem is different length. We will have to store the answer in the largest number possible but how to know which is largest in the begnining. So we store the answers to both linked lists and then finally when one list runs out continue in the other list. and return the head of that list.

        carry = 0
        dummy1, dummy2 = ListNode(0, l1), ListNode(0, l2)
        prev = None
        while l1 and l2:
            sum = l1.val + l2.val + carry
            carry = sum // 10
            sum %= 10
            l1.val, l2.val = sum, sum
            prev = l1
            l1, l2 = l1.next, l2.next
        if l1:
            while l1:
                l1.val = l1.val + carry
                carry = l1.val // 10
                l1.val %= 10
                prev = l1
                l1 = l1.next
            if carry:
                prev.next = ListNode(carry)
            return dummy1.next
        
        if l2:
            while l2:
                l2.val = l2.val + carry
                carry = l2.val // 10
                l2.val %= 10
                prev = l2
                l2 = l2.next
            if carry:
                prev.next = ListNode(carry)
            return dummy2.next
        if carry:
            prev.next = ListNode(carry)
        return dummy1.next
        