# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = right = dummy = ListNode(next=head)
        for _ in range(n): # 生成n个数字，执行n次
            right = right.next
        while right.next: # right走到末尾时,left在倒数第n+1个节点位置
            left = left.next
            right = right.next
        left.next = left.next.next

        return dummy.next
    
    # O(n);O(1)