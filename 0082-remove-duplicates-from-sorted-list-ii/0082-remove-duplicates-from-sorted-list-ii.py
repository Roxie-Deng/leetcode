# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev = dummy
        cur = head

        while cur: # 不能漏掉最后一个重复
            if cur.next and cur.val == cur.next.val:
                dup_val = cur.val
                while cur and cur.val == dup_val:
                    cur = cur.next
                prev.next = cur
            else:
                cur = cur.next
                prev = prev.next
        
        return dummy.next

# O(n); O(1)