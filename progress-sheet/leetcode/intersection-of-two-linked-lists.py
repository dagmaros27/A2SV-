# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        setter = set()

        first = headA
        while first:
            setter.add(id(first))
            first = first.next
        second = headB

        while second:
            if id(second) in setter:
                return second
            second = second.next
        
        