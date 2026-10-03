# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        count = 0
        while head:
            count += 1
            head = head.next
        count = count - n
        prev, head = dummy, dummy
        for i in range(count+1):
            prev = head
            head = head.next

        prev.next = head.next
        return dummy.next