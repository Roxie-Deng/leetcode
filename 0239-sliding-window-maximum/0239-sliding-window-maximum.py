class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 暴力: O(nk)
        # 在窗口移动的过程中维护一个数据结构，快速拿到当前窗口的最大值
        # 出队：下标不在窗口内; 值比新入队的要小（意味着永远不可能成为未来窗口的最大值）
        # 双端队列（存下标）
        # 并且保证单调性：下标递增，下标对应的值严格递减，dq[0]对应的值是窗口最大值
        dq = deque() # 存下标 (最大值候选下标)
        ans = []

         # 滑动窗口三步：入，出，记录答案
        for i,x in enumerate(nums):
            # 1.入
            while dq and nums[dq[-1]]<x:
                dq.pop() # 把队尾idx弹出
            dq.append(i)
            # 2.出
            if i+1-dq[0] > k: #窗口大小
                dq.popleft() # 把队首idx弹出
            # 3. 记录答案
            if i>=k-1:
                ans.append(nums[dq[0]])
        return ans
        # O(n);O(k)