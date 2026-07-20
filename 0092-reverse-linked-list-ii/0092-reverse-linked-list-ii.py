# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 1. 找到要reverse的头尾节点， 断链
        dummy = ListNode(next = head)
        start = end = dummy
        for _ in range(left-1):
            start = start.next # 例1中找到1
        for _ in range(right):
            end = end.next # 4

        very_start = start # 备份1
        start = start.next # 2
        very_start.next = None # 1,2 断链
        
        very_end = end.next # 备份5
        end.next = None # 断链4，5

        # 2. reverse
        def reverse(head: Optional[ListNode])-> Optional[ListNode]:
            pre = None
            cur = head
            while cur:
                # 备份nxt
                nxt = cur.next
                # reverse
                cur.next = pre
                # move
                pre = cur
                cur = nxt
            return pre

        new_between = reverse(start) # 从2出发反转；返回4->3->2

        # 3. 链接
        very_start.next = new_between # 1->4->3->2
        start.next = very_end # 2->5

        return dummy.next
        # O(n); O(1)