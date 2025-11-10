class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # O(log n): binary search [left,right]
        if not nums:
            return [-1,-1]

        # search scope
        left = 0
        right = len(nums) - 1
        # target index scope
        start = len(nums)
        end = -1

        # find min index
        while left<=right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                start = min(start, mid) # record current index
                right = mid - 1 # keep searching in the left half
            elif nums[mid] <target:
                left = mid+1
            else:
                right = mid-1

        # search scope
        left = 0
        right = len(nums) - 1
        
        # find max index
        while left<=right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                end = max(end,mid) # record current index
                left = mid + 1 # keep searching in the right half
            elif nums[mid] <target:
                left = mid+1
            else:
                right = mid-1

        if start==len(nums):
            start = -1
        
        return [start,end]