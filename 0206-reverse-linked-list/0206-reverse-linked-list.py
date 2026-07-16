# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # change all pointers' direction
        # pre - cur - nxt

        pre = None
        cur = head

        while cur:
            # 备份backup
            nxt = cur.next
            # 改向redirect
            cur.next = pre
            # 移动move
            pre = cur
            cur = nxt
        return pre
        # O(n);O(1)