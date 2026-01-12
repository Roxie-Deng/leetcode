# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next: # 保证fast.next.next两步都安全
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre # 反转方向
            pre = cur #向前推进
            cur = nxt
        return pre # 反转后链表头部

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return True

        # solution 1: create a list to store vals
        # solution 2: 寻找中间节点+反转后半段链表
        mid = self.middleNode(head)
        head2 = self.reverseList(mid)

        while head2: # head: 原链表, head2:第二半段链表（更短）
            if head.val != head2.val:
                return False
            head = head.next
            head2 =head2.next
        return True

    # O(n); O(1)