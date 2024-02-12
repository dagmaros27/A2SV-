# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        #collect the values in array and compare it with its reverse

        while head:
            arr.append(head.val)
            head = head.next


        if arr == list(reversed(arr)):
            return True
        else:
            return False
        