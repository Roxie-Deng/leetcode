class Solution:
    def maxSubArray(self, nums: List[int]) -> int: 
        # prefix f(i)=到i为止的和
        # f(i)最大-f(j)最小，if f(i)正f(j)负
        # f(i) - 0, if f(i)负f(j)负
        n = len(nums)
        prefix = [0]*(n+1)

        for i in range(1,n+1):
            prefix[i] = prefix[i-1] + nums[i-1]
        
        base = 0 
        ans = float('-inf')
        for i in range(1,n+1):
            ans = max(ans, prefix[i]-base)
            base = min(prefix[i],base)
        return ans
        # O(n);O(n)
        
