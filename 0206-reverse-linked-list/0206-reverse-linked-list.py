# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # change all pointers' direction
        prev = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = prev # reverse
            prev = cur # move nodes forward
            cur = temp
        
        return prev