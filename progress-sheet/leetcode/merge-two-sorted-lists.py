# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        one  = list1
        two = list2
        newL = ListNode()
        temp = newL
        while one and two:
            if one.val <= two.val:
                temp.next = one
                temp = temp.next
                one = one.next
            else:
                temp.next = two
                temp = temp.next
                two = two.next
        while one:
            temp.next = one
            temp = temp.next
            one = one.next
        while two:
            temp.next = two
            temp = temp.next
            two = two.next
        
        return newL.next
                
                

        