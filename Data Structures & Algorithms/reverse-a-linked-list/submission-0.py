# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# save the next element, point current element's next to last element

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l, r = None, None
        while head:
            r = head.next
            head.next = l
            l = head
            head = r
        
        return l