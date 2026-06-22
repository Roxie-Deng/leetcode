class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 不能使用除法； O(n)->不能嵌套
        # prefix[0] = num[0]
        # prefix[i] = num[i] * ...*num[0]
        # 再倒过来再算前缀积
        # rev_prefix[0] = nums[n-1]
        # rev_prefix[j] = nums[n-1]*nums[n-2]*...*nums[n-1-j]
        # i+1 = n-1-j
        # j = n-2-i
        # answer[i] = prefix[i-1] * rev_prefix[n-2-i], 0<i<n-1
        # answer[0] = 1*rev_prefix[n-2]
        # answer[n-1] = prefix[n-2]*1
        # 我们可以把prefix和rev_prefix再往前加一位[1]
        # 推导过程类似，最终结果: 
        # answer[i] = prefix[i] * rev_prefix[n-1-i], 0<=i<=n-1

        # answer[1] = 1 * (4*3)
        # answer[1] = prefix[1] * rev_prefix[2]

        n = len(nums)
        ans = [1]*n
        
        # 只用一个答案数组来节省空间，先从左到右
        for i in range(1,n):
            ans[i] = ans[i-1] * nums[i-1] # nums[i]的左侧乘积
        # 再从右到左
        rev = 1 # nums[i]的右侧乘积
        for i in range(n-1,-1,-1):
            ans[i] = ans[i] * rev # 左侧乘积*右侧乘积
            rev *= nums[i] # 更新右侧乘积
        return ans
        
        # O(n); 除ans外空间O(1)
