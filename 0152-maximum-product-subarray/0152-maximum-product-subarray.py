class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 不仅要维护当前位置最大乘积，还有最小乘积(遇到负数可能变为最大)
        n = len(nums)
        f_max = [0]*n
        f_min = [0]*n
        f_max[0] = f_min[0] = nums[0]

        for i in range(1,n):
            x = nums[i]
            # 三种状态：与之前最大乘积相乘；与之前最小乘积相乘；从当前位置开始
            f_max[i] = max(f_max[i-1]*x,f_min[i-1]*x,x)
            f_min[i] = min(f_max[i-1]*x,f_min[i-1]*x,x)

        return max(f_max)
        # O(n);O(n)