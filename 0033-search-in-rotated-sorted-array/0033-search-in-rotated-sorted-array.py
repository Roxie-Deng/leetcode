class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left<=right:# 保证检查完所有
            mid = (left+right)//2
            if nums[mid] == target: # mid
                return mid
            # always ascending, except max between min
            # 寻找target所在的有序部分，进行正常二分
            if nums[mid] < nums[right]: # right side on the mid must be ordered 
                if nums[mid]<target<=nums[right]: # [mid+1,right]
                    left = mid+1 
                else: # [left,mid-1]
                    right = mid-1
            else: # left side ordered
                if nums[left]<=target<nums[mid]: # [left,mid-1]
                    right = mid - 1
                else: # [mid+1,right]
                    left = mid+1
        
        return -1