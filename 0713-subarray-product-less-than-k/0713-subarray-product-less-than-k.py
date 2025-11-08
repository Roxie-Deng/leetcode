class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <=1:
            return 0

        cnt = 0
        left = 0
        prod = 1 # more elements, bigger product

        # expand the window: prod < k
        # shrink the window: prod >= k

        for right, num in enumerate(nums):
            prod *= num
            while prod >= k:
                prod //= nums[left]
                left += 1
            # for fixed right, count how many different left = count how many aubarray
            cnt += right-left+1
        
        return cnt