# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # before = []
        # after = []
        # curr = head
        # while curr:
        #     if curr.val < x:
        #         before.append(curr.val)
        #     else:
        #         after.append(curr.val)
        #     curr = curr.next

        # curr = head
        # i = 0
        # while curr and i < len(before):
        #     curr.val = before[i]
        #     curr = curr.next
        #     i += 1
        # i = 0
        # while curr and i < len(after):
        #     curr.val = after[i]
        #     curr = curr.next
        #     i += 1
        curr = head
        before = ListNode()
        after = ListNode()
        b = before
        a = after
        while curr:
            if curr.val < x:
                b.next = curr
                b = b.next
            else:
                a.next = curr
                a = a.next
            curr = curr.next
        b.next = after.next
        a.next = None
        return before.next
        