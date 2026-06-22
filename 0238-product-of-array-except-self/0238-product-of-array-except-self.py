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
        prefix = [1]*(n+1)
        rev_prefix =[1]*(n+1)
        answer = [1]*n
        for i in range(n):
            prefix[i+1] = prefix[i]*nums[i]
            rev_prefix[i+1] = rev_prefix[i]*nums[n-1-i] 
        for i in range(n):
            answer[i] =  prefix[i]*rev_prefix[n-1-i]
        
        return answer
        # O(n); O(n)