# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1.数长度
        n = 0
        cur = head
        
        while cur:
            n += 1
            cur = cur.next
        # 此时length是链表长度

        # 2. 辅助函数：翻转一组（k个）
        def reverse_k(node,k):
            prev = None
            cur = node
            for _ in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt 
            return prev # 新头
            # 此时cur是原链条上prev的后一个

        # 3. 分组处理，关键：链接表和移动指针
        dummy = ListNode(next = head) # 最终返回答案需要用的哨兵节点
        old_group_prev = dummy # 当前组的前驱节点

        while n>=k:
            n -= k

            old_start = old_group_prev.next # 当前组翻转前的头/翻转后的尾
            old_end = old_start
            for _ in range(k-1):
                old_end = old_end.next # 当前组翻转前的尾
            
            # 下一个要处理的组的头
            new_start = old_end.next
            # 断链
            old_end.next = None
            
            old_reversed_start = reverse_k(old_start,k) # 当前组翻转后的头，并且链表内部已翻转

            # 【入口-出口-移动】前驱接新头，旧尾接下一组，手移到旧尾处

            # 前驱是入口
            # 前驱->翻转头 必须先做。因为前驱本来指向的是old_start,要是它移动为下一组的前驱时带走的是old_start，之前翻转好的整组就丢失了
            old_group_prev.next = old_reversed_start
            # 翻转尾接新头
            old_start.next = new_start
            # 前驱指针挪到下一组组头前 
            old_group_prev = old_start
        return dummy.next