class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 前缀和 + 2Sum
        # 前缀和=从数组开头到当前位置的累计总和
        # 子数组的和sum(nums[left:right+1]) = prefix[right+1] - prefix[left] , prefix[0] = 0, prefix[1] = nums[0]
        n = len(nums)
        prefix = [0]*(n+1)  

        # 填充prefix
        for i,x in enumerate(nums):
            prefix[i+1] = prefix[i] + x

        cnt = defaultdict(int) # 前缀和:出现次数
        ans = 0

        for pre in prefix: # 0,1,3,6
            ans += cnt[pre-k] # 2Sum: k + pre1 = pre2
            cnt[pre] += 1
        
        return ans

        # O(n);O(n)