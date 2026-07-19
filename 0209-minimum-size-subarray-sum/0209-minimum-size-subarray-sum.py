class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # brutal: 遍历，找到所有满足条件的subarray,找出shortest
        # 滑动窗口，窗口内的和<target，移动右；满足窗口内的和>=target时，不断移动左，直到窗口无效

        ans = float('inf')
        cur_sum = 0
        left  = 0

        for i in range(len(nums)):
            if nums[i] >= target:
                return 1

            cur_sum += nums[i]
        
            # 满足窗口条件
            while cur_sum >= target:
                ans = min(ans,i-left+1)
                cur_sum -= nums[left]
                left += 1

        return ans if ans != float('inf') else 0
        # O(n);O(1)
