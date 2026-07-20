# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 找到要delete的节点在链表上的正数第几个
        # 1.链表长度
        dummy = ListNode(next = head)
        cur = dummy
        length = 0
        while cur.next:
            length += 1
            cur = cur.next
        # 2.m-th from the start
        # m = length - n + 1
        pre = dummy
        for _ in range(length - n):
            pre = pre.next 
        # 最后得到的pre是要去掉的点的前一位
        nxt = pre.next.next # 备份 要去掉的点的后一位
        pre.next = nxt # 连接

        return dummy.next
    
    # O(n);O(1)