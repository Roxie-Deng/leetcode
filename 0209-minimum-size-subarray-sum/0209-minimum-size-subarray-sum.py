class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = len(nums)+1
        left = 0
        cur_sum = 0

        # expand the window: cur_sum < target
        # shrink the window: cur_sum >= target

        for right in range(len(nums)):
            cur_sum += nums[right]
            while cur_sum >= target:
                min_len = min(min_len,right+1-left)
                cur_sum -= nums[left]
                left += 1
        
        return 0 if min_len == len(nums)+1 else min_len