class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k = k%len(nums)
        # nums[:] = nums[-k:] + nums[:-k]
        # 没修改引用但实际上在底层会创建临时代码
        # O(n);O(n)

        # 反转整个数组 -> 反转[0,k-1] -> 反转[k,n-1]
        def reverse(left,right):
            while left<right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        n = len(nums)
        k = k%n
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
        # O(n); O(1)