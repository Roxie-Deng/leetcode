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

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = self.middleNode(head)
        head2 = self.reverseList(mid)

        while head2.next:
            # loop condition works for both odd- and even-length lists:
            # when the list has an odd number of nodes, the middle node stays in place.
            nxt = head.next
            nxt2 = head2.next

            head.next = head2
            head2.next = nxt

            head = nxt
            head2 = nxt2