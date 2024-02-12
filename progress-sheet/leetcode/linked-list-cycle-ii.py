# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rab = head
        tor = head
        cycle = False
        while rab and rab.next:
            rab = rab.next.next
            tor = tor.next
            if tor is rab:
                cycle = True
                break
        if not cycle:
            return None
        
        curr = head
        i = 0
        while curr is not rab:
            curr = curr.next
            tor = tor. next
            i += 1
            if curr is tor:
                break
        return curr
        
        