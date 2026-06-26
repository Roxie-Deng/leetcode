# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        head0 = head.next # 第二个节点变新头
        head.next = self.swapPairs(head0.next) # 旧头指向新头后面的链表
        head0.next = head # 第二个节点指向第一个节点

        return head0
        # O(n);每次处理2个节点，递归深度n/2 O(n)
