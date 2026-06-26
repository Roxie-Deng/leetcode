# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 到底哪个神人会用链表存数字
    # 链表只能比较相邻的，联想到merge sort
    # 递归地把list劈成两半直到天然有序（只剩一个元素），再一层层向上合并
    # 第一步找链表中间节点
    def findMiddle(self,head:Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            pre = slow
            slow = slow.next # slow一次走一步
            fast = fast.next.next # fast一次走两步
        pre.next = None # 本题要做排序需要把链表断成两半
        return slow 
    # 第二步:合并两个有序链表
    def mergeSortedList(self,l1:Optional[ListNode],l2:Optional[ListNode])-> Optional[ListNode]:
        # 把两条已排序的链表按大小顺序拼成新的长链
        cur = dummy = ListNode()
        while l1 and l2:
            if l1.val<=l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        # l1 或 l2其中一个为空，另一个有余
        cur.next = l1 if l1 else l2
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: #递归终点，长度为0或1
            return head
        head2=self.findMiddle(head)
        #分治
        head = self.sortList(head)
        head2 = self.sortList(head2)

        # 合并
        return self.mergeSortedList(head,head2)

        # 递归深度logn,每一层所有子列表的总大小n O(nlogn);O(logn)