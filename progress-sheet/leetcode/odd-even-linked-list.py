# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        even = ListNode()
        odd = ListNode()
        o = odd
        e = even
        curr = head
        i = 1
        while curr:
            if  i % 2 == 0:
                e.next = curr
                e = e.next
            else:
                o.next = curr
                o = o.next
            i += 1
            curr = curr.next
        o.next = even.next
        e.next = None

        return odd.next


        