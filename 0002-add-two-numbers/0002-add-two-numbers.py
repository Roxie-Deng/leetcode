# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 每次循环往末尾添加一个节点。在第一次循环时，我们无法往一个空节点的末尾添加节点。创建一个哨兵节点
        cur_val = 0
        carry = 0
        cur = dummy = ListNode()
        while l1 or l2 or carry:
            s = carry
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            cur.next = ListNode(s%10)
            carry = s//10      
            cur = cur.next
        return dummy.next
        # O(n);O(1)