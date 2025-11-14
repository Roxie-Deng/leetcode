class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1. the array always goes uphill, except ans: nums[ans-1] > nums[ans]
        # 2. max, min are neighbors 
        if len(nums) == 1 or nums[-1]>nums [0]: # only one element or min is leftmost
            return nums[0]

        left =  0
        right = len(nums)-1

        while left<right:
            mid = (left+right)//2 # probable max
            if nums[mid-1]>nums[mid]: # in py, no index error
                return nums[mid]
            if nums[mid]>nums[-1]: # min in right part
                left = mid + 1 # mid impossible min
            else: # min in left part
                right = mid  # mid possible min
        
        return nums[right]
