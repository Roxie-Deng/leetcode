class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 双指针，slow:已排列好的序列尾部（左边全为非零序列）,fast:未排列好的序列头部
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
        
        # O(n); O(1):原地交换