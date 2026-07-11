class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 暴力：遇到0就把它和后面的非零数交换，like bubbling
        # 双指针: slow挨个遍历all，fast挨个遍历non zeroes
        # 把fast放到slow的位置，fast走完后，再把nums剩下的位置都填上0

        n = len(nums)
        slow = 0 # [0,len(nums_non_zeroes)]
        for fast in range(n):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        # 循环结束后slow = len(nums_non_zeroes)
        for i in range(slow,n):
            nums[i] = 0
        # O(n);O(1)