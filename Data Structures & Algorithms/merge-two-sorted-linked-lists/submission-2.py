# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # since deletion and updation of node is involved we keep a dummy node at the begining
        # this is always a best practise to avoid if else and conditional checks on head node

        dummy = ListNode(0, list2)

        prev, curr = dummy, list2

        while list1:
            while curr and list1.val > curr.val:
                prev = curr
                curr = curr.next
            prev.next = list1
            temp = list1.next
            list1.next = curr
            prev = list1
            list1 = temp # continuation of list1

        return dummy.next
