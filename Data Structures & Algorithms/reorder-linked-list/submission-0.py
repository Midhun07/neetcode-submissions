# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

    def find_nth(self, head, n):
        while n:
            head = head.next
            n -= 1
        return head

    def reorderList(self, head: Optional[ListNode]) -> None:
        # We split the list into 2 halves the first half we traverse noramlly and second in reverse. The cutoff if n // 2 if n is odd and n // 2 - 1 if n is even.
        # Then we traverse the nodes in the order specified and begin insertion.
        dummy = ListNode(0, next=head)
        count = 0
        while head:
            count += 1
            head = head.next
        if count % 2:
            count = count - (count // 2)
        else:
            count = count - (count // 2 - 1)

        k = self.find_nth(dummy.next, count - 1)
        rev = self.reverse(k.next)
        k.next = None
        head = dummy.next
        while rev:
            temp = head.next
            temp2 = rev
            rev = rev.next
            head.next = temp2
            temp2.next = temp
            head = temp
        
