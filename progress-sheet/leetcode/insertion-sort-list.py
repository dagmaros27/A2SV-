# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # arr = []
        # curr = head
        # while curr:
        #     arr.append(curr)
        #     curr = curr.next

        # arr.sort(key = lambda x: x.val)

        # for i in range(len(arr)-1):
        #     arr[i].next = arr[i+1]
        
        # arr[-1].next = None

        # return arr[0]

        curr = head.next
        dummy = ListNode()
        dummy.next = head
        dummy.next.next = None


        while curr:
            d = dummy
            while d.next and d.next.val <= curr.val:
                d = d.next
            temp = curr.next
            curr.next = d.next
            d.next = curr
            curr = temp
        return dummy.next

            


            
