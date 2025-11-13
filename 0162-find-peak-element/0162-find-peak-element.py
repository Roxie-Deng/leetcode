class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # O(log n): binary search
        left = 0
        right = len(nums) -1  

        while left < right: 
            mid = (left+right)//2 # 可能的峰
            if nums[mid]<=nums[mid+1]: 
                left = mid+1 
            else:
                right = mid # if nums[mid]>nums[mid],mid仍可能是峰，不能排除
        
        return left