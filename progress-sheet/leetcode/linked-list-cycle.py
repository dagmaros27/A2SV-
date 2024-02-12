# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        setter = set()
        curr = head
        while curr and id(curr) not in setter :
            setter.add(id(curr))
            curr =  curr.next
        if curr:
            return True
        else:
            return False
        