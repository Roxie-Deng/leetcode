# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy

        # move prev to the node just before the left
        for _ in range(left-1):
            prev = prev.next # original left-1
        
        cur = prev.next # the start of sublist, i.e. left node
        tail = cur # original left

        # reverse the sublist
        pre = None
        for _ in range(right-left+1): # the numer of nodes: reset every node's next
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        # reconnect the sublist to the original list
        # left-1 → right...left → right+1
        prev.next = pre
        tail.next = cur

        return dummy.next