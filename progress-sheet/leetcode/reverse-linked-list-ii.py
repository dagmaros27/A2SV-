# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        if not head or head.next is None:
            return head

        curr = dummy
        i = 0
        while i < left-1:
            curr = curr.next
            i += 1
        hold1 = curr
        prev = curr.next
        curr = prev.next

        while i < right-1 and curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            i += 1

        hold1.next.next = curr
        hold1.next = prev

        return dummy.next
            
            