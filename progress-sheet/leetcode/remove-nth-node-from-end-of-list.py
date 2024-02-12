# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # fast = 0
        # slow = 0
        # curr = head
        # while curr :
        #     curr = curr.next
        #     if fast - slow == n:
        #         slow += 1
        #     fast += 1
        dummy = ListNode()
        dummy.next = head
        length = 0
        curr = dummy
        while curr:
            curr = curr.next
            length += 1
        
        target = length - (n+1)
        curr = dummy
        i = 0
        print(length)

        if target == 0 :
            dummy.next = head.next
            return dummy.next

        while i < target:
            curr = curr.next
            i += 1
        curr.next = curr.next.next
        return head

        

            

        