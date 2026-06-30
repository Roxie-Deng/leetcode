class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # i不要当成下标，当成节点；nums[i] 不要当成值，当成指针，相当于i.next -> 有环链表
        # n+1个数，位置在0-n,数字范围在[1,n]。0必不可能在环内
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: # 快慢指针相遇，但不一定是环的入口
                break
        
        # 【【规律】】从起点到环入口的距离，等于从相遇点继续走到环入口的距离 
        # L起点到入环口，C环长，M入环口到相遇点
        # slow = L+M, fast = L+C+M, 2*slow = fast
        # L+M=C
        # L=C-M
        head = 0
        while slow != head:
            head = nums[head]
            slow = nums[slow]
        return slow
        # O(n);O(1)
    