# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        # fast moves twice as fast as slow
        while fast and fast.next: # nodes odd: fast none; nodes even: fast.next none
            slow = slow.next
            fast = fast.next.next
        
        return slow