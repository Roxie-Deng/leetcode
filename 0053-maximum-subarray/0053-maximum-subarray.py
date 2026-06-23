class Solution:
    def maxSubArray(self, nums: List[int]) -> int: 
        # 以第i位结尾的最大子数组和 
        # f(0) = nums[0] 
        # f(i) = max(f(i-1),0) + nums[i] 
        n = len(nums)

        cur = [0]*n
        cur[0] = nums[0]

        for i in range(1,n):
            cur[i] = max(cur[i-1], 0) + nums[i]
        
        return max(cur)
        # O(n);O(1)