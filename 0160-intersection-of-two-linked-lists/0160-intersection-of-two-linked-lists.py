# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 双指针+路径长度对齐
        # two-pointer + align the path lengths by letting each pointer traverse both lists
        curA = headA
        curB = headB

        while curA is not curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        # 相交，curA is curB
        return curA
        # 不相交，curA and curB最终都会走到空节点，curA is None
        # O(n); O(1)