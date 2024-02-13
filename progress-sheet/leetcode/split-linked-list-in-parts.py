# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        n = length//k
        arr = [n]*k
        rem = length % k
        i = 0
        while rem>0:
            arr[i%len(arr)] += 1
            i += 1
            rem -=1
        
        ans = []
        curr = head
        for i in range(k):
            j = 0
            part = curr
            while curr and j < arr[i]:
                curr = curr.next
                j += 1
            
            ans.append(part)
        for part in range(k):
            j = 0
            curr = ans[part]
            while j < arr[part]-1:
                curr = curr.next
                j += 1
            if curr:
                curr.next = None
            

        return ans

            