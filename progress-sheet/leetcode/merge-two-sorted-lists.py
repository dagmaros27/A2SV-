# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newLink = ListNode()
        curr = newLink
        def compareAndLink(list1, list2,curr):
            if not list1:
                curr.next = list2
                return
            if not list2:
                curr.next = list1
                return 
            if list1.val <= list2.val:
                curr.next = list1
                curr = curr.next
                return compareAndLink(list1.next, list2,curr)
            else:
                curr.next = list2
                curr = curr.next
                return compareAndLink(list1, list2.next,curr)
        compareAndLink(list1,list2,curr)

        return newLink.next


        
                
                

        