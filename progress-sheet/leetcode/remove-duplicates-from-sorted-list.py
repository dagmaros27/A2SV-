# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head

        while fast and fast.next:
            if fast.val == fast.next.val:
                fast.next = fast.next.next
            else:
                fast  = fast.next

        return head        