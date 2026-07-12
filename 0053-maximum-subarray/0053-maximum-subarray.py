class Solution:
    def maxSubArray(self, nums: List[int]) -> int: 
        '''
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
        '''
        # 继续优化: 不需要两次for和前缀和，可以实时DP，f(i)=到i时的最小子数组和，维护一个变量cur_max，状态转移：如果num加上cur_max反而变小，丢掉cur_max从num重新开始累加。再维护一个全局变量ans
        cur_max = 0
        ans = float('-inf')

        for n in nums:
            cur_max = max(cur_max+n, n)
            ans = max(ans,cur_max)
        return ans
