class Solution:
    def lowerbound(self,nums, target):
        # 返回 最小的 满足nums[i]>=target的 下标
        left=0
        right=len(nums)-1 # [left,right]
        while left<= right:
            mid = (left+right)//2
            if nums[mid]>=target:
                right = mid - 1
            else:
                left = mid +1
        return left

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # O(log n): binary search [left,right]
        start = self.lowerbound(nums,target)
        if start == len(nums) or nums[start] != target:
            return [-1,-1]
        end = self.lowerbound(nums,target+1)-1
        return [start,end]